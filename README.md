* politraf
  * systat.py - system statistic to clickhouse
  * connstat.py - connections statistic to clickhouse
  * constat.service and systat.service - config for systemd /etc/systemd/system/
  * politraf_clickhouse.json - grafana dashboard (Grafana 4.4)
* install
  * apt-get install tshark
  * pip install infi.clickhouse_orm
  * pip install pyshark
  * pip install pyyaml
  * mkdir /etc/politraf
  * cp config.yaml /etc/politraf/
* clickhouse - https://clickhouse.yandex/docs/en/getting_started/index.html#installation
* grafana - http://docs.grafana.org/installation/