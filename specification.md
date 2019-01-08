# Longtail Large Project Specification

A project file is a [YAML](https://yaml.org/spec/1.2/spec.html) file. All keys in the project file should be case insensitive and should be exclusively composed of characters in `[a-zA-Z0-9_-]`. Lowercase characters are preffered.

A project file must define the following keys:
- `project_name`, A very short (max 128 character) name for the project. Characters can be in `[a-zA-Z0-9_-]`
- `project_description` A short string (max 256 character) description of the project. String is normal for YAML
- `version` A [SemVer](https://semver.org/) style version number. The number must begin with `v` (e.g. `v1.0.0`)
- `sources` A map of places where the data may be found (e.g. Amazon S3). This is defined in greater detail below. The `sources` key must be present but may be empty.
- `files` A list of files in the project. This is defined in greater detail below. The `files` key must be present but may be empty
- `spec_version` The version of the `LLPS` spec used for this project file.

A project file may optionally define the following keys:
- `project_long_description`, A string literal of any length
- `author`, A string literal (max 256 characters) containing the name of the author
- `author_email`, A valid email address for the author
- `project_website`, A valid URL for the project

A project file should use the extension `.llps.yaml`

### Sources

Sources define where data is stored for a given project. Sources itself is a map from `source_name -> definiton`. Sources may not be named any of the reserved key names. All spec files must declare at least one source.

Each source must declare a `type` which must be one of the following:
- s3
- local
- tarball

Depending on the `type` the source must declare additional keys.

#### S3
Source keys:
- `bucket_name`, the name of the bucket
- `endpoint_url`, optionally specify an endpoint url. Defaults to aws

File keys:
- `remote_path`: optionally specify a path for the file within an s3 bucket. Defaults to `path`. It is not recomended to use a different path.

#### Local
Source keys:
- `hostname` the hostname of the system
- `root_dir` the directory from which all paths should be interpreted

File keys:
_None_

#### Tarball
Source keys:
- `file`, A file spec (see below) where the tarball can be found. Must rely on a different source.

File keys:
- `remote_path`: optionally specify a path for the file within the tarball. Defaults to `path`. It is not recomended to use a different path.
 

### Files

Files defines the files in the project themselves. Files a list of files. Each file is a map from `source_name -> file_source_schema_implementation` with the schema themselves defined in sources. Files must also include the the following keys:

- `path` A complete path for the file. Must be globally unique within the project (case insensitive). File paths are always interpreted relative to the `project_root`
- `md5` The md5 sum of the file. The md5 sum may be explicitly specified as `none`

Files may optionally define a `size` attribute listing the approximate size of the file with standard prefixes.

Files must specify at least one source (see above) and may define many.
