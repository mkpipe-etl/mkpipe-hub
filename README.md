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
- [PostgreSQL Extractor](https://github.com/m-karakus/mkpipe-extractor-postgres)
---

#### Loaders
- [S3 Loader](https://github.com/m-karakus/mkpipe-extractor-postgres)
- [Bigquery](https://github.com/m-karakus/mkpipe-extractor-postgres)
---


