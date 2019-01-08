# Longtail Large Project Specification

Bioinformatics projects are often composed of a large number of very heavy flat files. Managing these files is non trivial since operations take a long time and data loss is unacceptable. Because of the size of many of the files involved many typical tools for project management are not viable.

Tracking the files in a project and where they should be found is a core management task. This document details a file specification for tracking the files in a project. The specification file is intended to be placed at a top level directory for the project. The specification file is, itself, lightweight and version controllable.

## The Specification

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


### Sources

Sources define where data is stored for a given project. Sources itself is a map from `source_name -> source_definition`. `source_definition` may be (almost) any valid YAML but is intended to minimally define a storage location. The exception is that each `source_definition` must define a `file_schema`, a map from keys ([a-zA-Z0-9_-], case insensitive) to value types. Every file with the given source is expected to fulfill this schema.

Sources may not be named any of the reserved key names.

Note that `file_schema` may actually be empty in which case it will serve solely as a flag to indicate that a file should be found at a given source. Not all files must be present in every source. 

### Files

Files defines the files in the project themselves. Files a list of files. Each file is a map from `source_name -> file_source_schema_implementation` with the schema themselves defined in sources. Files must also include the the following keys:

- `path` A complete path for the file. Must be globally unique within the project (case insensitive). File paths are always interpreted relative to the `project_root`
- `md5` The md5 sum of the file.

Files may optionally define a `size` attribute listing the approximate size of the file with standard prefixes.

Files must specify at least one source (see above) and may define many.
