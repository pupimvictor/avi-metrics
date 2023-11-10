#----------Controllers to Poll Data From - REQUIRED ------------
#---------------------------------------------------------------
controllers:
  - avi_cluster_name: avi-controller
  #_comment: FQDN or IP address that the script will connect to for API calls
  avi_controller: 10.16.0.4
  avi_user: admin
  #_comment: ACCEPTS PLAIN TEXT OR BASE64 ENCODED PASSWORD
  avi_pass: *********
  tags:
  environment: prd
  location: sv05p
  #_comment: Realtime metrics will cause the script to take longer to complete, optional
  virtualservice_stats_config:
      virtualservice_metrics: True
      virtualservice_realtime: True
      virtualservice_runtime: True
      # virtualservice_names:
      #   - AutoScaleout-VS
      #   - Avi-DemoAvi-VS
      #   - WAF_Demo_VS
      virtualservice_metrics_list:
        - l4_client.avg_bandwidth
        - l4_client.avg_rx_pkts
        - l4_client.avg_tx_pkts
        - l4_client.avg_rx_bytes
        - l4_client.avg_tx_bytes
        - l7_client.avg_ssl_handshakes_new
        - l7_client.apdexr # Measures the clients view of the quality (response time and errors) of server responses. (VS)
        - l7_client.avg_application_response_time # Average server / application response latency. (VS)
        - l7_client.avg_blocking_time # Average time client was blocked as reported by client. Requires Client Insights set to Active. (VS)
        - l7_client.avg_browser_rendering_time # Average time browser spend rendering a web page. Requires Client Insights set to Active. (VS)
        - l7_client.avg_client_data_transfer_time # Average time required to transmit a file via layer 7 protocol (such as HTTP) from a virtual service to a client, excluding the Round Trip Time. (VS)
        - l7_client.avg_client_rtt # Average Round Trip Time between client and virtual service. (VS)
        - l7_client.avg_client_txn_latency # Client transaction time averaged across all HTTP requests. (VS)
        - l7_client.avg_complete_responses # Average rate of HTTP responses sent to clients per second. (VS)
        - l7_client.avg_connection_time # Average client connection latency as reported by client. Requires Client Insights set to Active to gather RUM data. (VS)
        - l7_client.avg_dns_lookup_time # Average DNS name lookup time as reported by the client. Requires Client Insights set to Active to gather RUM data. (VS)
        - l7_client.avg_dom_content_load_time # Average Dom content load time as reported by clients. Requires Client Insights set to Active to gather RUM data. (VS)
        - l7_client.avg_error_responses # Rate of HTTP error responses per second sent to clients. It does not include error codes that have been excluded in analytics profile. (VS)
        - l7_client.avg_frustrated_responses # Number of client HTTP requests that are completed but classified in the Frustrated latency bucket. (VS)
        - l7_client.avg_http_headers_bytes # Average size of HTTP headers per request.
        - l7_client.avg_http_headers_count # Average number of HTTP headers per request.
        - l7_client.avg_http_params_count # Average number of HTTP request parameters per request.
        - l7_client.avg_page_download_time # Page download time as reported by clients. Requires Client Insights set to Active. (VS)
        - l7_client.avg_page_load_time # Page load time as reported by clients. Requires Client Insights set to Active. (VS)
        - l7_client.avg_params_per_req # Average number of HTTP request parameters per request, taking into account only requests with parameters.
        - l7_client.avg_post_bytes # Average size of HTTP POST request.
        - l7_client.avg_redirection_time # Latency incurred by following redirects as reported by clients. Requires Client Insights set to Active. (VS)
        - l7_client.avg_resp_1xx # Rate of HTTP 1xx responses sent to clients. (VS)
        - l7_client.avg_resp_2xx # Rate of HTTP 2xx responses sent to clients. (VS)
        - l7_client.avg_resp_3xx # Rate of HTTP 3xx responses sent to clients. (VS)
        - l7_client.avg_resp_4xx # Rate of HTTP 4xx responses sent to clients. (VS)
        - l7_client.avg_resp_4xx_avi_errors # Rate of HTTP 4xx responses sent to clients from Avi, such as via custom security policies. This does not include errors excluded via the analytics profile or server generated 4xx errors. (VS)
        - l7_client.avg_resp_5xx # Rate of HTTP 5xx responses sent to clients. (VS)
        - l7_client.avg_resp_5xx_avi_errors # Rate of HTTP 5xx responses sent to clients from Avi, such as via custom security policies. This does not include errors excluded via the analytics profile or server generated 5xx errors. (VS)
        - l7_client.avg_rum_client_data_transfer_time # Total client data transfer time as reported by clients. Requires Client Insights set to Active to gather RUM data. (VS)
        - l7_client.avg_satisfactory_responses # Number of client HTTP requests that are completed and classified in the Satisfied latency bucket. (VS)
        - l7_client.avg_server_rtt # Average Round Trip Time between the Service Engine and server. (VS)
        - l7_client.avg_service_time # Average latency from the virtual services receipt of a request to start of the response. Requires Client Insights set to Active to gather RUM data. (VS)
        - l7_client.avg_ssl_connections # New SSL transactions per second (TPS), including SSL session reuse and failed handshake negotiations. (VS)
        - l7_client.avg_ssl_errors # SSL connection errors per second due to clients, protocol errors, network errors and handshake timeouts (VS)
        - l7_client.avg_ssl_failed_connections # SSL connection errors per second due to protocol, network, or timeout issues. (VS)
        - l7_client.avg_ssl_handshakes_new # New SSL transactions per second (TPS), excluding session reuse and errored connection attempts. (VS)
        - l7_client.avg_ssl_handshakes_non_pfs # New SSL handshakes / transactions per second (TPS) that did not use Perfect Forward Secrecy. (VS)
        - l7_client.avg_ssl_handshakes_pfs # New SSL handshakes / transactions per second (TPS) that used Perfect Forward Secrecy. (VS)
        - l7_client.avg_ssl_handshakes_reused # Successfully resumed SSL sessions per second. (VS)
        - l7_client.avg_tolerated_responses # Number of HTTP requests which had response latency classified as Tolerated per the virtual service analytics profile. (VS)
        - l7_client.avg_total_requests # Client HTTP requests per second received by the virtual service. (VS)
        - l7_client.avg_uri_length # Average length of HTTP URI per request.
        - l7_client.avg_waf_disabled # Average number of transactions per second bypassing WAF.
        - l7_client.avg_waf_attacksL Average number of WAF attacks.
        - l7_client.avg_waiting_time # Average waiting time reported by the client. Requires Client Insights set to Active. (VS)
        - l7_client.max_ssl_open_sessions # Maximum number of concurrently open SSL sessions. (VS)
        - l7_client.pct_cache_hits # Percent of HTTP requests served from cache. (VS)
        - l7_client.pct_cacheable_hits # Percent of HTTP requests that were eligible to be served from cache. (VS)
        - l7_client.pct_get_reqs # Number of HTTP GET requests as a percentage of total requests received.
        - l7_client.pct_post_reqs # Number of HTTP POST requests as a percentage of total requests received.
        - l7_client.pct_response_errors # Percent of 4xx and 5xx HTTP responses. (VS)
        - l7_client.pct_ssl_failed_connections # Percent of SSL connection failures due to protocol, network, or timeout errors. (VS)
        - l7_client.pct_waf_disabled # Transactions bypassing WAF as the percentage of total requests received.
        - l7_client.rum_apdexr # Quality (combination of performance and errors) of HTTP responses to clients based on RUM data. Requires Client Insights set to Active for RUM data. (VS)
        - l7_client.sum_errors # Total number of HTTP 400 and 500 errors sent to a client. (VS)
        - l7_client.sum_get_reqs # Total number of HTTP GET requests. (VS)
        - l7_client.sum_http_headers_bytes # Total size of HTTP request headers in a given metrics interval.
        - l7_client.sum_http_headers_count # Total number of HTTP headers across all requests in a given metrics interval.
        - l7_client.sum_http_params_count # Total number of HTTP request parameters.
        - l7_client.sum_num_rum_samples # Total number of samples used for RUM metrics. Requires Client Insights set to Active to gather RUM data. (VS)
        - l7_client.sum_other_reqs # Total number of HTTP requests that are not GET or POST requests. (VS)
        - l7_client.sum_post_bytes # Total size of HTTP POST requests.
        - l7_client.sum_post_reqs # Total number of HTTP POST requests. (VS)
        - l7_client.sum_reqs_with_params # Total number of HTTP requests containing at least one parameter.
        - l7_client.sum_total_responses # Total number of HTTP responses sent to clients. (VS)
        - l7_client.sum_uri_length # Total length of HTTP request URIs.
        - l7_client.sum_waf_disabled # Total number of requests bypassing WAF in a given metrics interval.
        - se_if.avg_bandwidth # Transmit and receive network bandwidth across all Service Engine interfaces. (SE)
        - se_stats.avg_connection_mem_usage # Percent of connection memory consumed. (SE)
        - se_stats.avg_connections # Rate of client network connection attempts (SYNs) per second across all virtual services for a Service Engine. (SE)
        - se_stats.avg_connections_dropped # Number of connections dropped or failed to establish across all virtual services for a Service Engine. Excludes drops due to a policy action. (SE)
        - se_stats.avg_cpu_usage # Hosts view of the Service Engines actively utilized CPU usage as a percent of total available CPU. (SE)
        - se_stats.avg_disk1_usage # Percent of Service Engine disk 1 capacity used(SE)
        - se_if.avg_eth0_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth10_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth11_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth12_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth13_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth14_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth15_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth16_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth17_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth18_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth19_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth1_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth20_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth21_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth22_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth23_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth2_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth3_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth4_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth5_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth6_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth7_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth8_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_if.avg_eth9_bandwidth # Transmit and receive network bandwidth for a Service Engine interface. (SE)
        - se_stats.avg_mem_usage # Percent of allocated memory used(SE)
        - se_stats.avg_packet_buffer_header_usage # Percent of all network packet buffers used. (SE)
        - se_stats.avg_packet_buffer_large_usage # Percent of large network packet buffers used. (SE)
        - se_stats.avg_packet_buffer_small_usage # Percent of small network packet buffers used. (SE)
        - se_stats.avg_packet_buffer_usage # Percent of total configured network packet buffers used. (SE)
        - se_stats.avg_persistent_table_usage # Percent of session persistence table used. (SE)
        - se_if.avg_rx_bandwidth # Received network bandwidth across all interfaces for a Service Engine. (SE)
        - se_if.avg_rx_bytes_dropped # Bytes per second of received packets that were dropped. Includes packets across all Service Engine interfaces. (SE)
        - se_if.avg_rx_pkts # Received network packets across all Service Engine interfaces. (SE)
        - se_if.avg_rx_pkts_dropped # Received packets dropped per second. Includes packet drops across all interfaces. (SE)
        - se_stats.avg_ssl_session_cache_usage # Percent of SSL session cache used. (SE)
        - se_if.avg_tx_pkts # Network packets transmitted across all Service Engine interfaces. (SE)
        - se_if.max_se_bandwidth # Maximum bandwidth through a Service Engine within the sample period. (SE)
        - se_stats.pct_connections_dropped # Percent of Service Engine connections dropped. (SE)
        - se_if.pct_rx_bytes_dropped # Percent of Service Engine bytes dropped. (SE)
        - se_if.pct_rx_pkts_dropped # Percent of Service Engine packets dropped. (SE)
        - se_stats.pct_syn_cache_usage # Percent of SYN cache used. Higher usage indicates too many incomplete open connection attempts. (SE)
        - se_stats.avg_dynamic_mem_usage # Percent of average dynamic memory used. (SE)
            
  serviceengine_stats_config:
      serviceengine_metrics: True
      serviceengine_runtime: True
      serviceengine_realtime: True
  pool_stats_config:
      pool_metrics: True
      pool_runtime: True
      pool_realtime: True
  controller_stats_config:
      controller_metrics: True
      controller_runtime: True
      controller_metrics_list:
        - controller_stats.avg_cpu_usage
        - controller_stats.avg_disk_usage
        - controller_stats.avg_mem_usage
  metrics_endpoint_config:
      - type: wavefront
        enable: True
        metric_prefix: "avi"
        #_comment: IP or FQDN for Wavefront
        instance: yosemite.wavefront.com
        #_comment:  If using direct ingestion specify an api_key, if no key then wavefront proxy will be used
        api_key: "94394c39-3a95-42e5-a0a7-501b673ad8ef"
        #_comment:  If using proxy specify the listening port, if not defined defaults to 2878
        proxy_port: 2878