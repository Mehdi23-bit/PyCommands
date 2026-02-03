from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class PylsArguments:
    arguments: Dict[str,Dict[str, Any]] = field(default_factory=lambda: {

       "-l": {
            "action": "store_true",
            "help": "use long listing format (permissions, owner, size, time)"
        },

       "-a": {
            "action": "store_true",
            "help": "show hidden files"
        },

       "-P" :{
            "action": "store_true",
            "help": "human readable sizes (use with -l)"
        },

       "-t": {
            "action": "store_true",
            "help": "sort by modification time"
        },

        "-r":{
            "action": "store_true",
            "help": "reverse order while sorting"
        },

       "-S": {
            "action": "store_true",
            "help": "sort by file size"
        },

        "-R":{
            "action": "store_true",
            "help": "list subdirectories recursively"
        },

      "-d": {
            "action": "store_true",
            "help": "list directories themselves, not their contents"
        },

       "--color": {
            "choices": ["auto", "never", "always"],
            "default": "auto",
            "help": "control colored output"
        },

       "path": {
            "nargs": "*",
            "default": ["."],
            "help": "directories or files to list"
        }

    })

