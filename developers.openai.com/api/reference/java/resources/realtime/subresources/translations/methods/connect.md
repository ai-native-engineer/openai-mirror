<!-- source: https://developers.openai.com/api/reference/java/resources/realtime/subresources/translations/methods/connect/ -->

## Connect

Open a Realtime translation session. The WebSocket URL requires a `model` query parameter.

**WebSocket** `wss://api.openai.com/v1/realtime/translations`

```java
import com.openai.client.okhttp.OkHttpClient;
import com.openai.core.ClientOptions;
import com.openai.core.http.HttpClient;
import com.openai.helpers.TranslationConnection;
import com.openai.helpers.TranslationWebSocketOptions;
import com.openai.models.realtime.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.time.Duration;
import java.util.Arrays;
import java.util.Base64;
import java.util.concurrent.TimeUnit;

// input.pcm: a short recording of 24 kHz, signed PCM16 little-endian mono audio.
public class Translate {
  public static void main(String[] args) throws Exception {
    long deadline = System.nanoTime() + TimeUnit.SECONDS.toNanos(30);
    byte[] pcm = Files.readAllBytes(Paths.get("input.pcm"));
    if (pcm.length % 2 != 0)
      throw new IllegalArgumentException("input.pcm ends in a partial PCM16 sample");
    try (HttpClient http = OkHttpClient.builder().build()) {
      ClientOptions options = ClientOptions.builder().fromEnv().httpClient(http).build();
      try (TranslationConnection connection =
          TranslationConnection.connect(
              options,
              TranslationWebSocketOptions.builder()
                  .model("gpt-realtime-translate")
                  .sendTimeout(Duration.ofSeconds(10))
                  .build())) {
        connection.send(
            RealtimeTranslationClientEvent.ofSessionUpdate(
                RealtimeTranslationSessionUpdateEvent.builder()
                    .session(
                        RealtimeTranslationSessionUpdateRequest.builder()
                            .audio(
                                RealtimeTranslationSessionUpdateRequest.Audio.builder()
                                    .output(
                                        RealtimeTranslationSessionUpdateRequest.Audio.Output
                                            .builder()
                                            .language("es")
                                            .build())
                                    .build())
                            .build())
                    .build()));
        // Wait for the language change before sending audio.
        while (true) {
          long remaining = deadline - System.nanoTime();
          if (remaining <= 0)
            throw new java.util.concurrent.TimeoutException("Waiting for session.updated");
          RealtimeTranslationServerEvent event =
              connection.receiveAsync().get(remaining, TimeUnit.NANOSECONDS);
          if (event.isError()) throw new IllegalStateException(event.asError().error().message());
          if (event.isSessionClosed())
            throw new IllegalStateException("Closed before session.updated");
          if (event.isSessionUpdated()) break;
        for (int offset = 0; offset < pcm.length; offset += 9600) {
          byte[] chunk = Arrays.copyOfRange(pcm, offset, Math.min(offset + 9600, pcm.length));
          connection.send(
              RealtimeTranslationClientEvent.ofSessionInputAudioBufferAppend(
                  RealtimeTranslationInputAudioBufferAppendEvent.builder()
                      .audio(Base64.getEncoder().encodeToString(chunk))
                      .build()));
        long finishTime = deadline - System.nanoTime();
        if (finishTime <= 0)
          throw new java.util.concurrent.TimeoutException("Translation timed out");
        // finishAsync sends session.close. Read the flushed text while it finishes.
        java.util.concurrent.CompletableFuture<RealtimeTranslationSessionClosedEvent> finished =
            connection.finishAsync(Duration.ofNanos(finishTime));
        while (true) {
          long remaining = deadline - System.nanoTime();
          if (remaining <= 0)
            throw new java.util.concurrent.TimeoutException("Translation timed out");
          RealtimeTranslationServerEvent event =
              connection.receiveAsync().get(remaining, TimeUnit.NANOSECONDS);
          if (event.isError()) throw new IllegalStateException(event.asError().error().message());
          event.sessionOutputTranscriptDelta().ifPresent(delta -> System.out.print(delta.delta()));
          if (event.isSessionClosed()) {
            finished.get(remaining, TimeUnit.NANOSECONDS);
            System.out.println();
            break;
      } finally {
        options.close();
