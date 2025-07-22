provider "datadog" {
  api_key = var.datadog_api_key
  app_key = var.datadog_app_key
}

resource "datadog_monitor" "cpu_high" {
  name               = "High CPU Usage"
  type               = "metric alert"
  query              = "avg(last_5m):avg:system.cpu.user{*} > 80"
  message            = "High CPU usage detected"
  escalation_message = "Please investigate immediately"

  thresholds {
    critical = 80
  }
}
