<!-- source: https://help.openai.com/en/articles/10929079-google-workspace-admin-managed-setup -->

# Google Workspace - Admin-Managed Setup

Updated: 10 days ago

To connect your Google Workspace to ChatGPT using admin-managed setup, you'll first configure access in Google’s admin consoles:

* **Create a service account** with read-only access to Google Drive, users, and groups.

  + This service account is strongly recommended to be created under the **same Google account that is associated with your ChatGPT Workspace**. If the accounts in the ChatGPT workspace have a different email domain than that used in Google Workspace, there are [additional steps you have to follow](#h_856676fdde) to enable this connector for your users.
* **Create an admin account** that the service account will act on behalf of.

Then, complete the setup in the ChatGPT admin console:

* **Upload the service account’s private key** (a JSON file from Google)
* **Specify the admin account** (no credentials required).
* **Select which files to sync** and **choose the users** who will have access to the connection.

This guide walks through each of these 6 steps.

# Setting up a Service Account

1. Navigate to [console.cloud.google.com](https://console.cloud.google.com).
2. Click on the projects dropdown.[Image](https://downloads.intercomcdn.com/i/o/dgkjq2bp/1444724631/7d007ed4cf25be3c6e75ab10b641/AD_4nXeIOJTMuQjZr38nYyDuzLEcJcWOdWZkTVnl4dCt3m8SylxRfpf-3xdL0C7VRU5v-7mf5kGwbfez25I_GBCHmDUJLODX1gOFpX7DfAcXhHmSsaa2laE3q4L0VjjxGRte7RK1kxilIA?expires=1764990000&signature=d75ed5f8b62d5258f9395d1b321852d0cbdd807fe49fe4825ec33afda848d96b&req=dSQjEs58mYdcWPMW3Hu4gbdd5t5xxhtV1AA%2BinX16nFkA1tUwYG7tyuA9hPo%0Awg%3D%3D%0A)Ensure you are logged into the same Google workspace as the one associated with your ChatGPT workspace (if you do not have a Google workspace associated with your ChatGPT workspace and have different emails between the two, you will have to [follow additional steps](#h_856676fdde), otherwise your users may not be able to use Google Drive synced connectors).
3. Choose **New Project**

![Google Cloud Select a resource dialog with dolores-lab.com organization selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-581aa8fad3694c782032d319/eba4bbb164ddca778cc4148921050e68/AD_4nXc6a8jbxWfRycNGY-MMAameZgWM0T_CsYY5iQPvRAuwbcWrGbDgjSgABtao7aJzLBE8JdGHd_0Sh6QrZdZbQVEwc_Ap_38eeRGjubCpPUmU4NvIf2lZxbU0lmzK)

1. Input a **Project Name**

![Google Cloud New Project form with organization dolores-lab.com selected and Create button available](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2cbdbf16380db83272d2188b/a0c18f4b04bc9a7e78752c1467b6b5fd/AD_4nXfZ56wrESi7peRZ3ALh_ilIpqWUBpO58x5s2MSEnrUlUXRlEhvXB5rVBpkPgIN757e1FusKL3Rz4jaMMYegdcKYgfu-o23C_gkAO9J6VmmYgJtWvQxJm611AkHJ)

1. Create the project

![Google Cloud New Project form with ChatGPT Google Connector entered under the dolores-lab.com organization](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-79c4d99a2afda6e1d798ce0c/9835ed3ce573a02f5ea4c5a2156a169f/AD_4nXdsbMWkaJBQ6STAKQqyvPsRUWYV07oBFZVV--Medrk5Sk1N6ETpuj5v76oVSYK-C1dQ1Gw0RpXF9i2DeNla468QhBrqdk93GthC-d1xsfRIYGJpflMwKXu_8zDp)

1. Wait until the project has been created, then click on **Select Project**

![Google Cloud notifications confirm creation of the ChatGPT Google Connector project for dolores-lab.com](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-158df62fe090ff79ec9a5113/cf09048c552670b4fdefa7dc124dee14/AD_4nXdt2u4Ojx6EShj6Q584ImObKZqZgJJMqKrtKhQlCde14BTVilj-9txMUNtR_YRfKjsod3nak3yy9fVORTy8mZPoctbRHVPuzCMtuB9u1y04kmhv5zlTYY7FXxHm)

1. Click on **APIs & Services**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-15a898b56882d47f4759f53a/35ea6f10fa3bcdf82917ad4c736172d1/AD_4nXfmDjmxglXmiBpIIPv1m_7E8xY0MZjIyJmB2V7NwTZYUR-_5uY6OVt0wgE23HZzPxdqrbi4lPQ7cLFYC3DFu29WZ7o_NJ_lwTYGgzyzSUWefj1DTEg0jX3CLcH3)

1. Click on **Library**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a7ddf322d4c6394b3eaa3110/90197302d76fe0ed2ee27ed1954a8821/AD_4nXc3RYJPXz9pYtqlRrwsUffnTolAWo-kOCiH3EfNcALMmVaEml1_EvlBwmRXaGT96BBH13dlAqCsZhhc9y0B_-fwZv6qiFAQyIh-Lk-Zew7Lsk_VtMz3vHXesjT6)

1. We’re now going to add three APIs, using the **search box** to find them

![Google Cloud API Library page with the ChatGPT Google Connector project selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-0b5d3874eeb79e2502c888cf/3b07a48919aaefaefcfa5ec96e712e77/AD_4nXe4xlXd74BmrK4gAysR4bB2whG1SPHmrC_U3mPpimpulOHL8CBjuKGumy7lRYBUJqe_idVwas3WU3_62VsVhSJuGLGLrVaPdqmlvqXHFNBLQ_qrku83TTVt92aG)

1. Search for and choose **Google Drive API**

![Google Cloud API Library search results for Google Drive API in the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-48f6954bc5a334e27af6e7b2/b27c044e4de497ce17a1a066d0fdd34a/AD_4nXcZcvPVFMl1AVkjQdR-noiIk21pW3oJWNeeWK43858sbZ4Q5FfAqdC7M6Kkl8_wyAlO6pR_-w1obqM483lrbnhY1joxRJSknOBuIsR_r_bYFbv--2PLSU2ZZqRW)

1. Click Enable

![Google Cloud Console Google Drive API page with the Enable button for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-683a506021f5d2ff86b02afd/4a332a979f0d1e3c3e305900643e7af1/AD_4nXczG9uD37jPsJf_oH--miKcMVDGFM8AQP3fluWqGBRv1k03BUG8vkQgnxq7yt4sJnBEnDbTx6GcQl60RsKAWssXoYtk--5vOIODXu-y4Ru52TpwnkC_FM4nxIX6)

1. Click on **Library**

![Google Drive API details page with the API enabled and Create Credentials available](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-fe247e5b861a5446542e3e33/cf3c6c99a344450b0d794c354951b383/AD_4nXdRyZmw8a-IHIF00-AbutVdn0ClrHqmOpuKQxXpwZJWgsdfAp5MRvkba32XeeNpAHQx7tp4KTwe_HctpvdV0I-N-dBIID33JdQ8xIr3We_khmMYnmT7I3RiZg00)

1. Search for **Google Drive Activity**

![Google Cloud API Library open for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e64366a1b2598c3833da51f5/c401d3a3bc6ff74a19a4f94c693063ca/AD_4nXc_j9-c6lohngLjIhaLZ2aMt7yWTGFDC3HUYUuizFbbCxboDuU-vFV8b2iykU_vn_7EirQins9b4o0dZd5fx26HXNhifQaXwNVmRwnNgP62TEnAgDqlzAl6c6_L)

1. Choose **Google Drive Activity API**

![Google Cloud API Library search results for Google Drive Activity API](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-033271441995dca571d4cf48/8c63aefb9e9008ebb03673d134ddec03/AD_4nXfRStKg6k1XxZF-qv7e-XhUG9oRHcgJcQrx8MGIPs0u3yAFTvH05keGrAJd36zFg_L37So8hiiCsmDY6agE9GdmFWjkVt39r_DzJB5O-xEqZcCCsKySmmNHgoNW)

1. Click **Enable**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-100299e0885ef3b08f5c67ce/9b3118669076ca88a675b729bd252c17/AD_4nXcZDKipHxGOyE2dQGlanGNbpu7323khTQvSeApSHHuqoIaV8O178jg-ayybbhNUY629KV0X8cZoWeiwHvXzOeM6ES1GLeL56J9KRKBtyaLyAMAt3LAF6QbAEwLH)

1. Click on **Library**

![Google Cloud Console Drive Activity API details page with the API enabled and Create credentials available](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-80dbfd6d1d190e668460317f/53da18f114ae78d08df0049fddcb5759/AD_4nXfTIV2kEYXrOifydAKAjo5xpAa700_hyMjjEQ4Ow-Qt9Sco9Jsu_FxiDYHEABeOK6OGeoXLW8zoG9iJ_9APwKdtZoeSEM8wtHfsnUSYjhKktbt5edDgTmeGfl7f)

1. Search for **Admin SDK API**

![Google Cloud API Library page for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-82186a14cfc4e265af3637ad/ebac87ed805c29121d5cae1d75ff17b7/AD_4nXeA1eIeE4oSIqGdKdnWnGIHFcGq7QB52ws784jHPjkYRh7OpDqmJyJHKxIkJiZCbGcHfDQgl4ApiRNiXoGHFTSseMkUpk_DH2_2fRYACvfRO8FaB6eNeLH2fHnN)

1. Choose **Admin SDK API**

![Google Cloud API Library search results for Admin SDK API with Admin SDK API listed](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-603fd9f432d8e0930d94c62d/40fb3f9321cc5c5913eab863fcd61450/AD_4nXeXdGADMaYZosklGXVpEyeKOYkpe_CxgGPGKRzGqdRA38BjVb-6PGzG3RydR_o556ZzyEPvKoTWpSKOt8w0IWYwgAOmkEYni0j6Ynkc7rc1hCi7MuP3Kda8SbdN)

1. Click **Enable**

![Google Cloud Admin SDK API page with the Enable button for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-ae7b938d824ca353032f7bc4/45af030c9c1be54b2e553fa076e89e41/AD_4nXe2Wll4aQk4F9Avr53FqlSW379l6UPwCfDI7uBK8n0dkhiXxy9XJNvGSf8bR--_dIPAwe-A_B_kH1eA6qK_cCWd71e7dmUhXK3zOnqtbIKu3iew12UDrRGv-CM2)

1. Click on **Credentials**

![Google Cloud Admin SDK API details page with the API enabled and Create credentials button available](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9abe16949410d4299a015a47/09911a209f5d03493700c448330c108a/AD_4nXef9I1EKjzU9VkePgMQsznn_OwD_84KKsGXdyIZKoP19ARCKn_oVooDysZYgdmgccXgcGnfEoKOJfkce4Wz0EoqeAkTOQ-O3vnNd92_SFHFmk7DPeQNSMUxMqax)

1. Click on **Create Credentials**

![Google Cloud APIs & Services Credentials page with Configure consent screen button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-f247b7ebc094272b3f1bde53/92605e9f757d891e934bc379865b4990/AD_4nXeQIbBFZc_e1n1z_xqR7LPPBy95woZmaLPHno1-OsPyD9VZDrajhG8KvL8_N-eJBnEuoIsReCqPo2vo3AkB2ftq3VkxBa7czQQ2EMz2j0Hv0IRbEvJ7b2nMy2SN)

1. Click on **Service account**

![Google Cloud Credentials page with Create credentials menu open for API key, OAuth client ID, or service account](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-44209eface41a27814f7b126/3464ca109c8c3a611f62c43a7d70bf17/AD_4nXfcSep-8PQ2zQYkW1Xcu49Izjyv0vXTIebMn8E8KVnkwW03H9vwdCLgd8diW9TdCBfXockL_oCiZ4cFLXECvVo3NfuEhFP9wRMobkSogcpvVO-2f_eyxExAyAzD)

1. Provide a **name** and **description** of your choice for this service account

![Google Cloud Create service account page with Service Accounts selected and service account details fields](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2faab3c9a2791b7838ef02f0/99e4180049c94e11e14634508db40577/AD_4nXeqK2-m21-fd5NtF738L98Rg5n2mkia9WMN4_OzPYZeoVMAJTR_QLm22zaNMtEM4VK--TtomVahzlpwXWJqgEqNs7xsyJEYlU79EQaXGF9c8lo_OzRRhbkG5f5O)

1. **(Optional)** You can assign a role - this is not required by ChatGPT.

![Google Cloud Create service account page with optional IAM role step and Service account created confirmation](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1edacff377e9b186d4a444af/5c9281745b1ef04ba38afaf0c7418cdb/AD_4nXdYU8k1hT8ZhvBBNOVL7uAdDvJGe2BcTL-1YSOgdjqAW2WutxqXgUxZ8VOG3vYqs_WmW-YjiUdv_j1wE2UAF5BxauFsMQlxgvpK4qN49EScR6VmWh-0TZpSsYQr)

1. **(Optional)** You can grant access to the service account - this is not required by ChatGPT.

![Google Cloud Create service account step 3 with Done button and Service account created confirmation](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-3584092ac99636854e6df0c1/e00e18e2a1b07acf3771611e032ea507/AD_4nXfnigYBpdJoQaYagGdQJ8KXeVdwWsFjTveORPW-fvSBTEsC4x63jlUCNesBLZi37V4QqIQGU9TDBJWHBQlAI1x8YhT7q8_PwpsylRd47PmLGoHjsD49DBzCZLlt)

1. Click **Done**.

![Create service account step 3 in Google Cloud with Done button and Service account created confirmation](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-ce0a5793b62a47e292f499ea/f9381ef240a2b3f5c28baf926c29602e/AD_4nXe-cJsFiU7tEADuGUJqI6oDfEYuKo-MG5A5j0SmCBuHWuVbodUEtrHR3Tv-y2cEGawTePFF6fhoehdNmdVKvc3_2PL0SWzSBIK24qc8LZXLEAgXYUKV8wZRbr3B)

1. Click on the **service account** which has now been created.

![Google Cloud Credentials page listing the newly created ChatGPT Google Connector service account](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-c8dbd6f35691094f17ac3ed4/2c6c30b792537c303db906cd7a902725/AD_4nXff2Anz055R6DeVzCJrWf4PIzjbXUVUERIPmoTOtBNPwnSmFsddGHIb4J4uxs0hyEQHdO64_LGSfejir9iA1ZxIpJZcHNDp6ZkFgK6gcyHApn7tpLtvpDBaWdyx)

1. Click on **keys.**

![Google Cloud IAM service account details for ChatGPT Google Connector, enabled after creation](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b8e1891c5bbb1eecae3e9bbd/1f05d22e2979823c731f9a02a7853ff2/AD_4nXeF0gaECHokw5_X_UWgQ22wzU6aRg_YZ32cB2ZXZRNJILVabh7lcDbV0Ip-0Aaj_jKn4oIgXG9ZrqvAXbxiA_SuFZuOk-lX17RDlpAAV69gQ4B772EriLm78sB1)

1. Click on **Add Key**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9bebe7a1232de98087b27b88/fa16f6eedc95527ab6f35275013072f5/AD_4nXdCfAIRUxxAs7aV15_nvQ9zw9S85yO72pOdZoQwcw63lO1RA6eVXyLlSFp8UWkZiDB71G4HTYmQX3da9vVLdMLN-4klm9n3d2Jrp-JkbIWxfpLNW7R1Eu1gD3va)

1. Click on **Create new key**

![Google Cloud service account Keys tab with Add key menu open to create or upload a key](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-df6f2fd37acc81bb69ffd858/6786b87965fb4ad7ec1afc6674c2c11e/AD_4nXf_9Bx3weJO_CmBm6pL-WeCVhTa2vp2JnmPlaLrpPZzQDTN21WfoNdWczPaiv6eRPh4LjgJRDtTfwMgSJVDHJKFQTt0-m0bL0LIvX_mssUJ1ze9wvcUDqieWEBk)

1. Keep the default JSON key type and click **Create**

If you see an error message that says “Service account key creation is disabled” follow [these steps](#h_482f106d88) to enable creation.

![Create private key dialog for ChatGPT Google Connector with JSON key type selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-47160a49c6645197584722df/e0dcd70600ab8f48cc3a24e40f1ac123/AD_4nXePKHL7dfbjXzQWOgJpsghCF6nHo61doPs4eyw05fHO3mM98z3NYZYr7ud7jwbvAH1l8G0RAwNGEezpn25BlbueIsgkZXOQZSPG2VHVuuoVkuE_p0FGfw54DUSb)

1. Click **Close**. The key has now been downloaded to your computer. You will later upload this to the ChatGPT admin console.

![Google Cloud service account Keys tab with confirmation that a private key JSON file was saved to the computer](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-7d969371c14a273c7d35a8b1/2dcf732aeb42becd1abe36f6d3fdacae/AD_4nXcg-bef6cTufiXr-mnHt8_LiUFlgcj2hOxO4YrU9dIXy6Yw0xKzapKJKQNA89y4TsWBKPtlBBfmdZq2UySeIg-SeFiE0M3zHntTzuqbIweDNgFej_oxlEBcgSEW)

1. Click on **details**

![Google Cloud service account Keys tab for ChatGPT Google Connector with Add Key button](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b9f27cd89686d99928acc1d2/eda7b76a4e14921ece2f07f09bb55c3f/AD_4nXdC19g1eHbGfslbz1ln7b4t9cuMKleKlthHXn9qYvWGhnVh-n-cDedJyaLgc5c67TyQIjtYZOqnC31z8nlXTl3fq4NuTr1GJqPKu1RMckwrTtGma3ibuFXIejJv)

1. Note that the **Unique ID**. This will be needed in Step 42.

![Google Cloud service account details for ChatGPT Google Connector with status Enabled](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-0f92bd1855af8f8ac32372a3/3d85f7ed27ef0b03c2fdc42e0b7eb979/AD_4nXeZCtBpX11_w1MYBVCGTE8JhpmFUlC2qTocAC-QCe1bozBUW3_PhN0lHR8AuKhx7cqDNisEz2mrFs_RsbA_Q1D47GKc12HA28kJmxEcLtDb9Rqi-kaV-BP1vm4Z)

1. Expand **Advanced settings**

![Google Cloud service account details for ChatGPT Google Connector with the account enabled](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-477bf683087e65511cd1327e/adf0cade51542f2270dbe8318d70d5ae/AD_4nXeZCtBpX11_w1MYBVCGTE8JhpmFUlC2qTocAC-QCe1bozBUW3_PhN0lHR8AuKhx7cqDNisEz2mrFs_RsbA_Q1D47GKc12HA28kJmxEcLtDb9Rqi-kaV-BP1vm4Z)

1. Scroll down and click on **View Google Workspace Admin Console**. The Google Workspace console will open in a new tab.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-009838f98a511cff542ceed9/0a6c870246dc413f3bce7fc78f95f741/AD_4nXf_vIoiknzRwk83Cw_3BvbCXMCelU8cfUtrNkJm4puGIJDW97iSwj7VCrc-0uBcDzyXAJLB1n5SgYyyB7oVTHj1jrSGoCdDsS_S2A3FddBcJawKLowMUtYjkKC3)

1. Click **Show more**

![Google Workspace Admin console home page for dolores-lab.com](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1db0b31758bc368b303dcb3e/54fbd4cf13064a6f5cbfbdb3ee70f86d/AD_4nXdjOSMDAHAhLtto7a1BgMmf9gQjiJp0jCMU7rLjYRxv3EivMuFNrZHSdw_db49Pf5MqWPoM_lPyEVdWw0AGhYqwrydgaIpXUnuD22cA1YDMkKmDyrUTeY8LGfTp)

1. Expand the **Security** section

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9114cc232e2f8e5e2346f291/0aa08d9fcb1eeb21f032f5ece8813214/AD_4nXfTIGVGFGPbitrnQ5OngOYFqE0gyP3CAl6kDCrvToIHLIFtLC0h58x3v_ARkr9QMIIpgeE6nucipLgUjNmwf6uQhJLrcYDrqyX5SIqPs-_BIHRTzfjXDPjyC4NI)

1. Expand the **Access and data controls** section

![Google Workspace Admin console home with Security section expanded in the left navigation](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e45343c67f2d3d0e4f6cd895/432c6d9bfb23c990f9a1a5f5988b97ba/AD_4nXd_ndyYt-IAHmzuLWosaNNJjybuy9ieuARmyoSbJrTiR78oXqvVehkrna__J79Zaxy_xIPUOUDWv5kOWCh_xQ_e-AnNEaCNZkZnBKAOKMUbEGpR8pqYOC3L5p1U)

1. Click on the **API controls** section

![Google Workspace Admin console home with Security > Access and data control expanded in the sidebar](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-811c66b0353c0d6bbbf5d6a4/4fe067426bac73d2b754cc904ba51658/AD_4nXdR4nLx-qfbxZkMquobYazVGHHv4q0VA5_YWviygG0Bydt03b2XtRUhvVrFflh5IInPV3w5sX4L3sgUZ0hdMeU2iQN9BEx8dEGE_nNk502ymJTX8uyTAaLRXwr7)

1. Click on **Manage Domain Wide Delegation**

![Google Admin console API controls page under Security > Access and data control](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-66d38e5784050cbedaec185d/3a26c5de01f6a383e81f548cd2b06327/AD_4nXd6WEGuW_95SQji_HrgPhIqhHbByzj5wPQbERPJHm9z4dGUxeEogmruj1eusw93x4Laqg8h9S5UkAjpTsJ49ftQS5TSdxBLUvBPrhH_HXTIQFtdZNf45mSBaacf)

1. Click on **Add new**

![Google Admin Domain-wide Delegation page with API clients list and Add new option](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-01889b7699f748d234a44b11/5447b04a2bca514dad14928458dc91ed/AD_4nXeE1U1TZl5x4y_1KEbirgESj1yEu5ac3_gIMuGu2E-0W4d8ck2_C6eNm9Y8HNWSFMureRop_D17zQ5ZCyBO1X3dRm5mjqpv34xii5l_sJS15MpGag_XayHA9zjs)

1. Use the **Unique ID** previously noted as the value for this **Client ID**

![Google Admin Domain-wide Delegation dialog for adding a new client ID and OAuth scopes](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-8b10ebf2f8da06416d3fc2d9/dbe6e8491c35551a6445dec141c9c28d/AD_4nXcnnLlIIAWny8dGTmR62EP36Gp2J2UZqnacoorKyN0AfYogsVA0neVl5fIDess3y50qtxKMwUAZ26fXX5YIvCcT8ZgRSzlTi0kkvetZ-BLIj7-CJdfOSNhwpTbn)

1. For the **OAuth scopes**, refer to the following comma de-limited auth scopes values that you'll need to copy and paste:

```
https://www.googleapis.com/auth/admin.directory.group.readonly, https://www.googleapis.com/auth/admin.directory.group.member.readonly, https://www.googleapis.com/auth/admin.directory.user.readonly, https://www.googleapis.com/auth/admin.directory.user.alias.readonly, https://www.googleapis.com/auth/drive.activity.readonly, https://www.googleapis.com/auth/drive.metadata.readonly, https://www.googleapis.com/auth/drive.readonly, https://www.googleapis.com/auth/userinfo.profile, https://www.googleapis.com/auth/userinfo.email
```

|  |  |
| --- | --- |
| **Scope** | **Reasoning** |
| [admin.directory.group.readonly](https://www.googleapis.com/auth/admin.directory.group.readonly) | enforce group-based permissions |
| [admin.directory.group.member.readonly](https://www.googleapis.com/auth/admin.directory.group.member.readonly) | enforce group-based permissions |
| [admin.directory.user.alias.readonly](https://www.googleapis.com/auth/admin.directory.user.alias.readonly) | handle cases where the user is granted permission via an alias |
| [drive.activity.readonly](https://www.googleapis.com/auth/drive.activity.readonly) | to be notified when changes occur to files |
| [drive.metadata.readonly](https://www.googleapis.com/auth/drive.metadata.readonly) | sync file content and associated metadata (ex. last modified date) |
| [drive.readonly](https://www.googleapis.com/auth/drive.readonly) | sync file content and associated metadata (ex. last modified date) |
| [userinfo.profile](https://www.googleapis.com/auth/userinfo.profile) | determine the users for whom we’re syncing files |
| [userinfo.email](https://www.googleapis.com/auth/userinfo.email) | determine the users for whom we’re syncing files |

![Google Admin Domain-wide Delegation dialog for adding a new client ID and OAuth scopes](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-1d1a6a3ef8d0269dcdf5d41c/e4e33462af057ad6c2afd7212f8a6d39/AD_4nXczrMULPRrBpF2bkbfVKFabl47OdiVmyv6gwHCrNejQhU4JY8T70nNhoZYTHPGcBahmjaaoao1nfHquJ7HkFulfDxbllnkVsLUnaVruD4m-PY6SXdyB6qcP2FSO)

45. Click **Authorize**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-4c6695fb47ff907ec3e22d27/c51b096aab5d23dd9c3cc4a2bbdb114e/AD_4nXezLrI8q-TS4avHfPxJU5oxZlfBZEIhhvKr7g-mRHK46G8kT-dVMXhRo8Zzn36iYtS3JwyszopeC-f7KkzqeAqnn6YbCT8rkS8HzPbtTq4z6CC3jaWtkLnxAI_J)

46. Success!

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-19a43c98b2ce3d9d56d6291e/9d62615b907e55417ce37b36cff57d41/AD_4nXc7Tr3O1PMFGN_BGRVO3awWQ50V-nJmhiM-k0GOIdswM1-ixUZw08PAkft-KqY4AL_z-Jv883epgK3KA27jcLg5DPZnBV5-rYvR1jmMetDTG-yCKxePof0V248l)

# Setting up the Admin Account

1. Expand **Directory**

![Google Admin Domain-wide Delegation page with a ChatGPT API client and scopes listed](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-671569a263fe134836b50edd/ade724d5dee6c168818389b85572d751/AD_4nXc7Tr3O1PMFGN_BGRVO3awWQ50V-nJmhiM-k0GOIdswM1-ixUZw08PAkft-KqY4AL_z-Jv883epgK3KA27jcLg5DPZnBV5-rYvR1jmMetDTG-yCKxePof0V248l)

1. Click on **Users**

![Google Admin domain-wide delegation page listing a ChatGPT Google Connector API client and scopes](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d7b5b736d314623e6273dd66/8716a98aa0f27ecc949491ff5e13ca03/AD_4nXcJ22e89pSupWiMKmXkv9gODGwr0kDcULGGEYkJeFu2PLGXalIsCgs1CORPpdPRFQAdY1hq06ws_ZbJR1j5kJDyLeIFVK2l7qJyZi4gkZxqu0zldmMHC4HNYT_t)

![Google Admin console Users page listing workspace accounts for setup and management](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-29783ed5558fcc8a5785f61a/b9f567883a1660dfaa038cf705267932/AD_4nXeQpc2GWE6BWfxdJEmgO1zfXaU6CSaJA-IaiOOLVGvAVTdyuHKc7I_GRom1SvRwUN2QRPZTZL3yNy0dWliTcHaTJVsZUkI-CMbOM7VSDFGlgluhx0HKDpNyeQ6k)

1. Provide a **first name**, **last name**, and **primary email** address of your choosing

![Google Admin console Add new user form for creating a Workspace user at dolores-lab.com](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-d1bbf6d8daaf1c65f5c99e55/3a98d863bef6ccdb35c6ca5087e4cbb4/AD_4nXdjjrKoTKxuscAhFSngH8ltNC_j_0Wqts00zXR6w2OX73iO3Anhs7Yw-ThWS-GC_-90b4VF26B5-13kHRXERaGrTxPSKTe8tBfHDkzoGwgYvbD63XONno17S47P)

1. Click **Add new user**

![Google Admin console Add new user form filled for a ChatGPT Connector account](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b67a5b1a1b9bc73f8d233361/112f8925e0b6acffffa204bce423f6f3/AD_4nXfaokAnIRVKsGPTjdT4bVRVRg7B03ln3CIjm5FfiOzFX68YrZVuaN6I8f6PMcLWzyZw6kNih9qkpYSQxo2QfrKZfGnSy24DreqVU5xpOedWelw_JJufZ93NOlKx)

1. **(Optional)** Record these credentials. ChatGPT does not need these credentials.

![Google Admin Console New user added page for ChatGPT Connector with Copy Password and Done actions](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-0ce10d761d4f3fb2bbc1b250/97f3c1264d2ac5d0a79de00f7d322ab7/AD_4nXch_eMxj37M22UDEwDN4iD50kna75yizbsnmiZKYyIIc4YX8RulcnJBRXg4PBiZ_pyWrhJ41E3LrPtmJhC3IzVMAt6-O2kRVNBR-60t60ytTCJ8MaGaEAIz2HrM)

1. Click **Done**.

![Google Admin console Copy password dialog for a newly created user account](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e24fb233e0ba725202e3c153/bf03f7bdd91e3eb182f85efa62a21512/AD_4nXfcS8SYnX34ZqXertWdndWSA32bmZVdKCFHTIkPne8fBScKSlmLLhQ6IC4ox9BjjS5qhUMsv6V1axql_srzOrqff8IRPHp8PFvm6pbI8_0cCVOokaeWr_qeghQo)

1. Click on the **account** you just created. If it does not appear in the list, refresh the page or clear your cache and cookies and try again.

![Google Admin console Users page listing accounts including ChatGPT Connector](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9062b9a27660dcb8a0ad9913/dec084c0ed08d5f182283d0d83307fff/AD_4nXcm4x9OCyckdYVxdoHsYGrGfpcYFbOmkeJHSuxf5SyaKOSZZvPDCkhK3ZsAafxoNYuaxhZMLxtl44LP9yeOdrkVODn4n1w9mnYUUbDOnsFID4PaiBMbs_9z2uMx)

1. Click on **assign roles**.

![Google Admin user details page for the ChatGPT Connector service account](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-70afa53bb8ff3e3694b714b7/761b9bc0c92f49093e298e96ced35722/AD_4nXf8KSLyihMiQJq17KWSPbtXMTYJuA05Cn0N02L0AJbIHlABrE7nMD_Lr6-7V5fWG-OWQAmhcedlFOonUe1xuDWf5ZJkP7Ptkq7eHyabnalMC22MDOlix7iD9xLE)

1. Toggle on the **Groups Reader, User Management Admin,** and **Storage Admin** roles.

![Google Admin ChatGPT Connector user page with Admin roles and privileges open and no roles assigned](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-50ca4ee1ba89e5b14c9301e5/d23a873ba65044ab0551a926fab880de/AD_4nXdmSpXTaXxOegJ0DMlpAqa3RgJqmgqL4xCHWqkt_4YZUw9jpzbf5WYtbChR7T-GhFFTXkjo7m-7e705N902brxkefHT11UJ8AWpIUR1SUhEE4vnkm14-OUEGjte)

1. Scroll down and click **Save.** The admin account has now been successfully created and configured.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b5fdfafca514a74b3ae26356/7bf6f501cb8139572b3640f0b78daa88/AD_4nXcRFcFOPdvxRfd5ZrFaiPXTLwwqTKbrRriS-_FmXZ3Q2z6oDkAHtOO5cNQpEZW_xr7TEKGdUXlY39w4QozT5heHMO2VkENWWHtljxzY4CqCFKdeqOh2WpO3Tk1F)

# Completing setup on the ChatGPT Admin Console

1. Navigate to ChatGPT and click on the profile icon on the upper right corner of the page.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-878aee9275117d10047116fd/da3acaaabfc9f7271e04b0b162bab425/AD_4nXcbm37xTjnbYl9iiEu2sq5T0nv2BuDANCbsxDcWKFhutAC26GEmwTVvdg02xnRtn90at7EAPDCTfl5G7cO8AqYddqiMELpoei_PD5NgA8B1Lx1fR8DnPjhcX_-r)

1. Click on **Manage workspace**

![ChatGPT workspace menu with Manage workspace selected under the organization switcher](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-47d9fb889151e003fd5b47eb/de540874077d7bc510ea9590c3697ae7/AD_4nXe5RteINSPIEZe7HM_ZUrfXcl7q-MXkb4lorpNp4FZXzPzuUbb3BYhVedLKlBXSOpqiCkTpgRnBL1FQysWTAFVFNoKQd9GgiffqtLx_Ong-dUTjGBJ2M9jaFTOH)

1. Click on **Connections** and then under **‘Synced connectors’** → **Enable** **Sync**

![Connectors page with Google Drive sync prompt and Enable Sync button highlighted](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b1de3173aa5e3effddf47a60/f72451f3bf716903684f1e1e8ba40d99/AD_4nXc7Gc8XLZzodOBoDRr-e5UVJd4JnSyipJtDiawnSyEEnFD2daMk8ErFz_wST8fz93xLSW34xhOSFdlGDZ1NInm-QBUXqI5CNzlcbb8kgIpbEW8FzqQ8afvoC68n)

1. Ensure **Admin-managed** is selected and click on **Next**

![Google Drive connection setup with Admin-managed setup selected over Self-service setup](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-630da85520fdf50cecffe45c/64d4e17e5f515b796dc6e4cc9467e8f5/AD_4nXdOsK9-EJgC3xAx56sM4WVKnTY94aDa3QipsUXfzHNAT6KYOTBlytk9VKJCvjsurJLwULA9sZghdJN9WkrAWYopsx5N5No7fng0oSAQ7gh3rKevd0A0qeUNVD-w)

1. Type in a **display name**. We recommend using the name of your Google Workspace.

**Please note that we currently do not support changing the name of your connection.**

![Google Workspace connector setup dialog with display name Dolores Labs entered](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-73520cb8f5641797ae8b03fb/70e515214c56ff29a17dd29ceb9fb90b/AD_4nXfcBXhPqtOIlsBQSMorWAXZy90XJssMryttuamuAgHbAucaCQqzQf-ekl_Z1HeXY4G8-aJETzDyauQeBGmbri9kxuEMndLOaUiHXjIWdb4t6sozZD2WuPpIFDJy)

1. Click **Save Draft and Continue**

1. Click **Upload key**. Choose the JSON file, which is the key you downloaded as part of setting up the service account above. Ensure this key is accurate

![Google Workspace connection setup step prompting upload of a service account key and admin email address](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e22a6b3549149dfc0c555e8a/cfb27cdf9b6bf1df44a596ed9ea81849/AD_4nXe3azMef8nSmJmZ5Y0vzXoc_k5zGjwi15_cBMR_5ou45WUea4GAFzEiho4t93UDzl67cLfqb--6aCrAYhSPW6len1Vern1t_hoj9WFsJKlReOzIQFnvrxLxc70w)

1. Type in the **admin email address**. This is the admin account you created previously.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-ad77fe64819003462faaa845/eaadbea4d1aac5c3c8c4e5227a9ce028/AD_4nXcE8hL899xfsYJ3f5svUejEYYfG1bZ3Tc4UmnkMPZT6dSIY1-HT-_JAvROpXZw_L4wMGRwo1uVsMZE5bJhZeNU2DXRhYkqLMc-69n4PEQtX2cFlgAKhxYcimIFP)

1. Click **Save.**

![ChatGPT Connections credentials dialog with service account key and Google Workspace admin email entered](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-32f4e99026bb35cab63548e6/777d940234182481450dd03b592daa86/AD_4nXeHVnV-3_7oBkF2ShhFYRY8zfUPMA1mVBHydACPuH8FIBeFYe7BK2iA6FHCpLKA7NMw2uhBOX6O2mT01IIS6DMFAaKWQeBRvn7XJRk1CyUN6lKlcRciIYmI-heg)

1. Choose whether you want the files in all of your users’ My Drives to be included.

![ChatGPT Connections modal for User files with Include user My Drives enabled at step 2 of 5](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-3ebf46e3ebf45f7d70071098/e4209ac63943bb51dcc1f00937126191/AD_4nXeyL0A7-RHQD4JxhWJMQNKeAfGQKqpkAVKK4SIlGAO4gzJQU3pNynVxfWTLlwQO0Bqjd5bZtaDmvINNuo_vCzN24OGzHgtDv3EwNH4EG5o92aL17b2uwmr58ton)

1. Click **Next**

![ChatGPT admin Connections modal for User files with Include user My Drives enabled in step 2 of 5](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-bebe5217772970cc3ba62b05/5e3d5e5aa9070c192a64801d4abc3e62/AD_4nXeyL0A7-RHQD4JxhWJMQNKeAfGQKqpkAVKK4SIlGAO4gzJQU3pNynVxfWTLlwQO0Bqjd5bZtaDmvINNuo_vCzN24OGzHgtDv3EwNH4EG5o92aL17b2uwmr58ton)

1. Choose how to manage shared drives. We support the following three scenarios:

1. If you want to include all shared drives, then choose **Include by default** and do not add shared drive IDs to be excluded
2. If you want to include most shared drives, then choose **Include by default** and add the IDs for the shared drives you want excluded
3. If you want to exclude most shared drives, then choose E**xclude by default** and add the IDs for the shared drives you want included

![ChatGPT admin Shared drives setup with Include by default selected and an Excluded Shared drives field](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e85208bc4e3f905a69009544/324e51fbeed12752ac8e98aa8caa8f8e/AD_4nXck05X4oZthzaJf43D8uxSalS8QAzLEO99r5QbdPswxpq4RyE_bh4RhT61AQAOkMoeC-Sj_of1YmzTrvHMbTV6I0W7ojIVH3ppYvl4tm8dFNt5XmBkrFWUveqvh)

1. To look up the ID for a shared drive, navigate to it in a web browser. The **last portion of the URL** is the shared drive ID.

In the following example, it is `0ADvY03uUbEcQUk9PVA`'

![Google Drive shared drive with Manage members visible for Example Shared Drive](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9b17140b1b68ec7d03e3887a/a4d83441ae99f099a37801a65401fcb7/AD_4nXcklrN4kIUZ782vQnkeLlq9ZvMsuWx-BdP0RJg1dOcHy_sWkDYcCv5KcCrQcuXPRv6OrLdAClp28nRzhD9STvkX4Gl5AbxPFvTS44I2FTcrjykbHjjwIjHZswXt)

1. Click **Next**

![ChatGPT admin Connections modal for Shared drives with Include by default selected at step 3 of 5](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e593e41d0fa396a12ab4735c/dd12e81579e3c2927136236b6f6e5719/AD_4nXck05X4oZthzaJf43D8uxSalS8QAzLEO99r5QbdPswxpq4RyE_bh4RhT61AQAOkMoeC-Sj_of1YmzTrvHMbTV6I0W7ojIVH3ppYvl4tm8dFNt5XmBkrFWUveqvh)

1. Choose who should have access to the Google Drive connection. You can either select Admins of the ChatGPT workspace only, or enable it for everyone. If enabled for everyone, new users added to the workspace will automatically be included.

![Google Drive connector permission set to Admins only for workspace members](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e709e77040715b1347a5b075/eeccbd2606c522738ec71ee5e172066a/image.png)

1. Click **Start syncing**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-64a8cec65a29764902a4d905/0564ecc28f050ba8220d599ca97c212b/AD_4nXfN4CKr1zZa1rGre89W7wb0EqxIg3WW81i5DDNbhbFTKg8nungoC6oumZQ2oYqjEk8L_nYGiSZf5rE4mlfXtmVhk63PtQieNIZvi2nV11YeY1H3GplYNRCQz4dP)

1. Your Google Drive connection has now been successfully created!

Please note that, while it will start syncing immediately, it can take hours to days to complete depending on how many files were included based on your settings. Once files added/edited in the past 30 days have finished syncing, the connector will become available to the users you enabled it for.

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-50a52a00c8c69bd6cd02cc6d/b3a553ab41d29baddcb2b79ac398a3f2/AD_4nXcaO25roB7RQwnzWSTcT9na5I5G4wLmG0nYYoH_coCCQRS2Us6gQJc06ER5885p_MLDyWTvyZed2SZDJAseYHdHMDmPBrIL-sjWc8xWK7nElQrYjnIo7AmDx8hq)

# Enabling service account key creation

If you receive the following error, you will need to enable service account creation for this specific project:

> The organization policy constraint ‘iam.disableServiceAccountKeyCreation’ is enforced on your organization.

![Google Cloud service account Keys tab with error that service account key creation is disabled](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-86d778c6b885a8c342170e98/7b34ad5fbd8d8066996de442062a6f17/AD_4nXdnMzIwwXZ-aUzOnPMpOXzmjexuk7ynNiG6-mNXzUiFIJkN57sW73p5hp_drO1sOd7IunA93IdxcvxaqFlxmSTqK8vHJMf8TQAsObNTbVo7BqKHyVHyJen4HDhN)

1. Open up a new tab and navigate to [console.cloud.google.com](https://console.cloud.google.com). Make sure the selected project is the one you’ve already selected.

Click on the **menu icon** in the upper left corner.

![Google Cloud Console welcome page for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-e4e55ebc5080a6e5a566d205/a5a968468a4ffb7b2ce04415de2f3425/AD_4nXd1xlHjHDLcbf_qxaAQppEnDXJzQkf7rwpyr8WVMF3uQqG0Ea-M5nG0KYu1WEmPWWvaoV4HPelgGx3Y0q1KzmfHRnvZ8XDDOvQ2HkxYcLr6K_FDClHWjNbMporv)

1. Hover over **IAM & Admin**

![Google Cloud Console navigation with IAM & Admin open and Organization Policies selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-faa2a980174b1a54336efd39/f8248f8c870bdb17b2e946f15cdde2ef/AD_4nXeXQkhDmb6sgh1ba9Cv_NalYaccOun3MvHNrxoSuLwI6vXehpnHFkfx4B4VTRabksjQ1-3Uu3zaGw1FDkeyaAw_Gi91wMsV0t2cHawYcC-rpnsd0E1rkqaJof2v)

1. Click on **Organizational Policies**

![Google Cloud Console IAM & Admin menu opened to Organization Policies](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-2458ff83727b6d5bc4e74a20/b76a82ec7e5442380b87643956a2e2cd/AD_4nXeXQkhDmb6sgh1ba9Cv_NalYaccOun3MvHNrxoSuLwI6vXehpnHFkfx4B4VTRabksjQ1-3Uu3zaGw1FDkeyaAw_Gi91wMsV0t2cHawYcC-rpnsd0E1rkqaJof2v)

1. Search for **iam.disableServiceAccountKeyCreation**

![Google Cloud organization policies for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a089106f9b0ea143f29f3740/ffaa4bf2a21ca01ec3b71dd29821f103/AD_4nXcIjd3ue48c_Tsb3YAN-pNHbO6M2eE4DoQN1ZqZAsvr2td87bQMBjgonx3Wymlj0497BLSqxbdRfMZgV03Z_aOH8_Y2HG5Mi9p_SjPNRyWAbLtHeFLt0fN-_CJ6)

1. Click on the result for **constraints/iam.disableServiceAccountKeyCreation**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-aff625a4a95795acfed2761e/1876c87809f75ce79fb256b5716a43c0/AD_4nXfq7r3ZkTPcQO1vAM0GuOhShfOUp46eMKj_sK36V554Zrcp8JIN-OxLgAFwKM_Ji9TMW1frsQwIcwEC424jZ5O9KokmSJGSuEYKIJjQDmJXW_wS8uiuih1zp4FV)

1. Click on the … for the row with the ID of **iam.disableServiceAccountKeyCreation**

![Organization policies filtered to Disable service account key creation for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-f4d2f3fc2a6a18cf7ffc13b9/b5a378fca2d75abc1f25707ecd2fa652/AD_4nXdCCz0pDkvRWWbjyvJPymB-P4PmR6h2PWNUT-iOGwCszkG-GvWeHxWLsL1t1RvcvO5SmJdJRCq7RabbgL7ANV7-8YQ8owj_GxvOP3BeJQgY746BV5a3ga9A1HLE)

1. Click on **Edit policy**. If Edit policy is disabled, you’ll need to become an Organization Policy Administrator.

![Google Cloud Organization Policies filtered to Disable service account key creation with Edit policy menu open](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b30553c589d499d25d8be07a/ef514949d638cbf85b0242453529c589/AD_4nXda8bPHVRcAyidXdVaL9vb_VkO6Wzq_g6c5qPnLCPetdXfrhJQR6x9L6BJ8S9mpx4n7_T64L9tAk4mVYWuapR2dyVU3s6thS7-CBHGam-4GhFU_cVJehXSqIlmX)

1. Click on **Override parent’s policy**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-cb2515366fd3b1cc4e0b12c8/f4696069b1f5eda3b333db2fbd0016e6/AD_4nXciiigtvigmO0o5pHN0T34jkVELXUPllY05usn_i7wcLeclFR-HM5T6JL3Y-KR0z4K-ZLW4KSnTHYhgVVd6fqSn-H5LlWMA1DvVjZl4qVqpVeSfs3DJTHt4k6Y4)

1. Click on **Add a rule**

![Edit policy page for Disable service account key creation with Override parent's policy selected](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a5e3836d27793f3844034795/4f59451d3c66191c0fccef3170986003/AD_4nXfk3rQ0bEHn6XZ95Q7Eg_qtnnROrtCIvMYKXrfrea2El-Oe5B7tXB-SR_vomP06yg70BPRnxOzRA4r1AgKt58HEdBtCTA-nIT1UaMB3NJb1thPyUWijdDaTiXSU)

1. Click on **Set Policy**

![Google Cloud Edit policy page with Override parent's policy selected and enforcement set to Off](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-ac9f082f4a6e0548d807c609/12ed5162a0762749148365fb1ef5b6df/AD_4nXfFZYCNVSr56coSnDH6J45VJSCFai0fg5fwHeMEiTS5iXQDkbwbOY-SHT6U3ZZ2ZkNttvMfi7aC5NlbZn7WCRvLb_72F1JPyHievLPIrw1h1xODRoinnIic_2K1)

1. You can now create a service account key. This enablement may take several minutes to take effect.

![Google Cloud policy details with Disable service account key creation set to Not enforced](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-c686b41ca22f2d83baa7d114/afbd61565a688d1ee626689fc6ca8eb1/AD_4nXcZPNSv6HDTbmRMZWQ30Tt6Hf-xH8fMjVHnkXjYx122AVag8rcaxBcU1aehIy89rpgzn-krrzxPzUWj-1TQHJqtdT1FqeL3bsv5TqWWZG7Qz2pDFm3_pj0bRHCR)

# Becoming an Organization Policy Administrator

1. Navigate to [console.cloud.google.com](https://console.cloud.google.com) and click on the **project/organization selector**

![Google Cloud welcome page for the ChatGPT Google Connector project](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-c4143d14bcbba58a0065dde1/1f06ff10fdc690f437cc44ef1e6af8d6/AD_4nXd1xlHjHDLcbf_qxaAQppEnDXJzQkf7rwpyr8WVMF3uQqG0Ea-M5nG0KYu1WEmPWWvaoV4HPelgGx3Y0q1KzmfHRnvZ8XDDOvQ2HkxYcLr6K_FDClHWjNbMporv)

1. Click on **your organization**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b47ba46847bf6a7b22bd37a9/ca5d07fb4c0445bc7181f95e94ffa0f1/AD_4nXcdXOuVy7NBy_YP6j8qlfeTns7mWQPJbBO9FuyXNgBA_tXmUpESvi0kpKkpPNwd9LH-iiXT2HUVVjNhmZfUQGIHrFIH03c45KoC6UN8l_bQNbJXr9dyJwth_Bgv)

1. Click on the **menu icon** in the upper-left corner

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-aca4a66263c181800fbf3c75/c2c3b25e8abcffb08725f87aaa28fcbb/AD_4nXce5BwZgvd_TQumLynPCPlzl3oUsgXNUbnXt2annIW2sNa4uAyi5ThsljDYq0qtkO7cxbMA4SosoVO5sm3MInsGevK7pQzajC1ijE-UooCNwVinnwgZt_fPf_ak)

1. Hover over **IAM & Admin**

![Google Cloud console navigation menu open with Google Cloud Setup pinned](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-a2f4b427ce570d2555ac2c12/b8fa95d0e71f48a02f7d5335037fbc13/AD_4nXdtIGodxa98NbVQcBfnI53sX3VAfemMhrEQ4uhfzm4z_5fPdX0QP4Xl-__NPtjTrTLV0X3F4mSprcnuYsf_EM0v1qpxPsBf2zJgBGVi71KsXhGFMBG3EOc5pxO3)

1. Click on **IAM**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-cd3c8dfdf6011f3996c30126/7cf2114ebaa2f1638ccbb752b14a181a/AD_4nXc53O0Py156ua_e9vk5odr7hYxxOwTb0VR75E5HnzYffLejw2fNjwJlOhKKuKU_eRtxrZ7DJquBYhv8fq3lRCM5flq60BxnAS2hHhesveE9Fg81Hk6amOGwuhEe)

1. Click on the **pencil** for your account

![Google Cloud IAM page for dolores-lab.com showing organization permissions and the Grant Access action](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-0fc6f7b1cd6c3932c211edbf/3f04b1b38130843607c1e42cbd9ef10c/AD_4nXf5Pqt62EECOGvh57gxaHtespYtP6W3ritfm7d2frysTvFZU8NruLXBsrFY5L1zv6OwsWWPXsvyxJubuFmxpotzXAhNqwMsdwcEvJqmrOwCZwuLGv7kxp1_qH7l)

1. Click on **Add Another Role**

![Google Cloud IAM dialog assigning the Organization Administrator role for dolores-lab.com](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-dfeff89c2287f181be28f9c3/fda97e52ac0adebc14886b49deeafc54/AD_4nXfkGcDXGgVMccsC9yWeqZ6niKQr9SflLMdW1pRfYy2ubL8vXpXjgD6qtXYu4hUupJHK2i89ibrdhT-vNHYH7YgO-FY79VPjJ8Ws8MRm1sErgE_IFGjnL1dUimEd)

1. Search for **Organization Policy Administrator**

![Google Cloud IAM edit access dialog assigning the Organization Administrator role to a user](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-291ec9d49269c3b32ac19b93/07f46f272965849ab71914865b007486/AD_4nXdfUnb0B3vgQdmsxv7oW-MQRIsLXtfGl7QsZIbtTj1irpsB_FtZtS44RzbWrd-tTA-0s3qdvaZSupkn2DEKNhGOrDu55bZBAbFdiPiWfn6UpYThPBOzv1_lFW8X)

1. Click on **Organization Policy Administrator**

![Google Cloud IAM role picker with Organization Policy Administrator selected while editing access](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-755d23454ce550fbdb3a8e78/7673442d085023c32d17e0d6541134f4/AD_4nXf6e8MSOcC7BnaEKhuWkCenJi43cBN3I85sYHyeFnW7y84-b-LMtJrI_m048p506z0Q3Cf8hIrkvl_zKN6ywMjTC0WIClQbPJVBZMOzTnNJqRTE2ZYvNc6Frms8)

1. Click **Save**

![Google Cloud IAM access editor assigning Organization Administrator and Organization Policy Administrator roles](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-9d9304f9c99cd45f229d57ad/f7f6fba94053e91c4f6fae30d19f888f/AD_4nXdfa2pmq_ZPi8uPbsn1reItJHyEmA6qmUWmTkMD-Ne_XdQbKP8SF9_ZasmhKXqRhB0nlQLOmN5Esu9ail3uiir26fDiuoMVcgzr64Dn-yJ38jbzYaJfqGTT-xDh)

1. Your account now has permission to enable service account key creation. This may take several minutes to take effect.

# Using a Google Email Alias to Maintain Different Email Accounts for Google Workspace and ChatGPT

If you're an admin connecting Google Workspace to your ChatGPT workspace using the [admin-managed setup](/en/articles/10929079-internal-knowledge-google-workspace-admin-managed-setup) for Google Drive synced connectors, and your organization uses **different email domains** for ChatGPT and Google Workspace, you’ll need to take additional steps to ensure users can successfully access Google Drive synced connectors.

**Recommendation**: Whenever possible, use the same primary email addresses for both Google Workspace and ChatGPT accounts.

If this isn’t feasible, follow the instructions below to configure a Google Workspace email alias that matches the ChatGPT sign-in email.

## Steps to Add a Google Workspace Alias

Follow these steps in the **Google Admin Console** to ensure each user's ChatGPT email can be linked to their Google Workspace account:

1. **Go to the Admin Console.** Navigate to: **Directory > Users**

![Image](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-42a89cc5b4744e47d9a91372/83e0090e08dd217b3f8bad30f1ebf52d/AD_4nXdkszGaG8UY8u2tKQWpz06dfqmXlPrMwWWjs6J9VHnvUlZMblYillj1aqndKoOpLut_4iDq_0HKEPqR3SLBIXOdY8_qDVlcn_bxhnx-K6R9IKOg-TyxCDw6as3r)

1. **Select a User,** then “ADD ALTERNATIVE EMAILS”.

![Google Admin user details page with Add alternate emails action highlighted](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-6cd224b6de534075525f12b5/7e9727f62b78b90cb7a7e17d29fb9116/AD_4nXed9-j3pId9cFlUbBCmFfMGsE4mS-3O3x_eugfNNTPppVGNskrNR7Pu9pDB8OJfw18A_PnKLmYUP5HlHPxbHtkEQRj-Ps9n9OhS1D3zE9seq2mf77YhHofA0gxo)

1. Add an Alternative Email. **Ensure it corresponds to the user’s ChatGPT account.**

![Google Workspace Admin alternate email alias form with alias-testing-alt-email on bytesheaven.com](https://images.ctfassets.net/j22is2dtoxu1/intercom-img-b7a881c6e4b6d95708a811f1/593b898b5e70d406e3cc7bd018f851a1/AD_4nXeMFckeryDpG3PpzU4mQEIZJgjL-2hd-6dCfDOJ2xaFi7FAG0kySq_LPudwSFIh3D1uc5Va6XFb50Z2W2_aPLcM-jPIveYvtbMXDh0wmLr86aNzSe_PbHOD6Kuc)

1. Select **Save**

---

## Known Limitations

### Personal email addresses are not supported

Users who register for ChatGPT using personal addresses (e.g., example@gmail.com) cannot connect to Google Workspace. This setup is unsupported and presents a security risk, as it enables access to internal data from outside the organization.

### Gmail "+" aliases are not supported

Gmail allows users to create aliases by appending a "+" to their address (e.g., `user+alias@gmail.com`). This type of aliasing does not work with Google Drive synced connectors. The alias must be explicitly configured in Google Workspace.

## Common Error Message

If email addresses are not properly linked, users may encounter this message: "We were unable to connect your account to Google Drive. [Click to learn more](#h_856676fdde)."  
  
If users receive this message, review the steps in this document and ensure they are followed accurately. If additional assistance is needed, please [contact our support team](/en/articles/6614161-how-can-i-contact-support).
