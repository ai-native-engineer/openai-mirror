<!-- source: https://developers.openai.com/api/reference/go/resources/realtime/subresources/translations/methods/connect/ -->

## Connect

Open a Realtime translation session. The WebSocket URL requires a `model` query parameter.

**WebSocket** `wss://api.openai.com/v1/realtime/translations`

```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"log"
	"os"
	"time"

	"github.com/openai/openai-go/v3"
	"github.com/openai/openai-go/v3/option"
	"github.com/openai/openai-go/v3/realtime"

func main() {
	if err := translate(); err != nil {
		log.Fatal(err)

func translate() error {
	// input.pcm: a short recording of raw 24 kHz mono signed PCM16 little-endian audio.
	pcm, err := os.ReadFile("input.pcm")
	if err != nil {
		return err
	ctx, cancel := context.WithTimeout(context.Background(), time.Minute)
	defer cancel()
	client := openai.NewClient()
	connection, err := client.Realtime.Translations.Connect(ctx, realtime.TranslationConnectionOptions{}, option.WithQuery("model", "gpt-realtime-translate"))
	if err != nil {
		return err
	defer connection.Close()

	if err := connection.Send(ctx, realtime.RealtimeTranslationClientEventUnionParam{
		OfSessionUpdate: &realtime.RealtimeTranslationSessionUpdateEventParam{
			Session: realtime.RealtimeTranslationSessionUpdateRequestParam{
				Audio: realtime.RealtimeTranslationSessionUpdateRequestAudioParam{
					Output: realtime.RealtimeTranslationSessionUpdateRequestAudioOutputParam{Language: openai.String("es")},
	}); err != nil {
		return err
	// Wait for the language change before sending audio.
	for {
		event, err := connection.Recv(ctx)
		if err != nil {
			return fmt.Errorf("translation ended before session.updated: %w", err)
		switch message := event.AsAny().(type) {
		case realtime.RealtimeErrorEvent:
			return fmt.Errorf("translation failed: %s", message.Error.Message)
		case realtime.RealtimeTranslationSessionClosedEvent:
			return fmt.Errorf("translation closed before session.updated")
		if event.Type == "session.updated" {
			break
	for offset := 0; offset < len(pcm); offset += 9600 {
		end := min(offset+9600, len(pcm))
		if err := connection.Send(ctx, realtime.RealtimeTranslationClientEventUnionParam{
			OfSessionInputAudioBufferAppend: &realtime.RealtimeTranslationInputAudioBufferAppendEventParam{
				Audio: base64.StdEncoding.EncodeToString(pcm[offset:end]),
		}); err != nil {
			return err
	// Close the session to flush remaining audio, then read the final translated text.
	if err := connection.Send(ctx, realtime.RealtimeTranslationClientEventUnionParam{
		OfSessionClose: &realtime.RealtimeTranslationSessionCloseEventParam{},
	}); err != nil {
		return err
	for {
		event, err := connection.Recv(ctx)
		if err != nil {
			return fmt.Errorf("translation ended before session.closed: %w", err)
		switch message := event.AsAny().(type) {
		case realtime.RealtimeTranslationOutputTranscriptDeltaEvent:
			fmt.Print(message.Delta)
		case realtime.RealtimeErrorEvent:
			return fmt.Errorf("translation failed: %s", message.Error.Message)
		case realtime.RealtimeTranslationSessionClosedEvent:
			return nil
