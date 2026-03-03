# mkpipe-hub

`mkpipe-hub` is the central registry for all official and community-contributed plugins for the `mkpipe` ecosystem.  
Here, you can discover extractors, loaders, and utilities to extend your `mkpipe` workflows.

---

## Plugin Registry

The main plugin registry is maintained in [plugins.yaml](plugins.yaml).  
This includes details about all available plugins and their metadata, including repositories, PyPI links, and descriptions.

---

### How to Contribute

If you’ve built an extractor or loader for `mkpipe`, feel free to add it to the registry by following these steps:
1. Fork this repository.
2. Add your plugin to `plugins.yaml` using the format below:
   ```yaml
   extractors:
     - name: "PostgreSQL Extractor"
       repo: "https://github.com/m-karakus/mkpipe-extractor-postgres"
       pypi: "https://pypi.org/project/mkpipe-extractor-postgres/"
       author: "m-karakus"
       description: "Extract data from PostgreSQL databases."

   loaders:
     - name: "S3 Loader"
       repo: "https://github.com/m-karakus/mkpipe-loader-s3"
       pypi: "https://pypi.org/project/mkpipe-loader-s3/"
       author: "m-karakus"
       description: "Load data into Amazon S3."
   ```

3. (Optional) Add a `.md` file to the appropriate folder (`extractors/` or `loaders/`) with detailed documentation.
4. Submit a pull request!

---

### Explore Plugins

#### Extractors
- [PostgreSQL Extractor](https://pypi.org/project/mkpipe-extractor-postgres/)
- [MySQL Extractor](https://pypi.org/project/mkpipe-extractor-mysql/)
- [MariaDB Extractor](https://pypi.org/project/mkpipe-extractor-mariadb/)
- [SQLite Extractor](https://pypi.org/project/mkpipe-extractor-sqlite/)
- [SQL Server Extractor](https://pypi.org/project/mkpipe-extractor-sqlserver/)
- [Oracle DB Extractor](https://pypi.org/project/mkpipe-extractor-oracledb/)
- [Redshift Extractor](https://pypi.org/project/mkpipe-extractor-redshift/)
- [ClickHouse Extractor](https://pypi.org/project/mkpipe-extractor-clickhouse/)
- [Snowflake Extractor](https://pypi.org/project/mkpipe-extractor-snowflake/)
- [BigQuery Extractor](https://pypi.org/project/mkpipe-extractor-bigquery/)
- [MongoDB Extractor](https://pypi.org/project/mkpipe-extractor-mongodb/)
- [Cassandra Extractor](https://pypi.org/project/mkpipe-extractor-cassandra/)
- [TimescaleDB Extractor](https://pypi.org/project/mkpipe-extractor-timescaledb/)
- [DynamoDB Extractor](https://pypi.org/project/mkpipe-extractor-dynamodb/)
- [Elasticsearch Extractor](https://pypi.org/project/mkpipe-extractor-elasticsearch/)
- [InfluxDB Extractor](https://pypi.org/project/mkpipe-extractor-influxdb/)
- [Redis Extractor](https://pypi.org/project/mkpipe-extractor-redis/)
- [File Extractor](https://pypi.org/project/mkpipe-extractor-file/)
---

#### Loaders
- [PostgreSQL Loader](https://pypi.org/project/mkpipe-loader-postgres/)
- [MySQL Loader](https://pypi.org/project/mkpipe-loader-mysql/)
- [MariaDB Loader](https://pypi.org/project/mkpipe-loader-mariadb/)
- [SQLite Loader](https://pypi.org/project/mkpipe-loader-sqlite/)
- [SQL Server Loader](https://pypi.org/project/mkpipe-loader-sqlserver/)
- [Oracle DB Loader](https://pypi.org/project/mkpipe-loader-oracledb/)
- [Redshift Loader](https://pypi.org/project/mkpipe-loader-redshift/)
- [ClickHouse Loader](https://pypi.org/project/mkpipe-loader-clickhouse/)
- [Snowflake Loader](https://pypi.org/project/mkpipe-loader-snowflake/)
- [BigQuery Loader](https://pypi.org/project/mkpipe-loader-bigquery/)
- [MongoDB Loader](https://pypi.org/project/mkpipe-loader-mongodb/)
- [Cassandra Loader](https://pypi.org/project/mkpipe-loader-cassandra/)
- [TimescaleDB Loader](https://pypi.org/project/mkpipe-loader-timescaledb/)
- [DynamoDB Loader](https://pypi.org/project/mkpipe-loader-dynamodb/)
- [Elasticsearch Loader](https://pypi.org/project/mkpipe-loader-elasticsearch/)
- [InfluxDB Loader](https://pypi.org/project/mkpipe-loader-influxdb/)
- [Redis Loader](https://pypi.org/project/mkpipe-loader-redis/)
- [File Loader](https://pypi.org/project/mkpipe-loader-file/)
---


