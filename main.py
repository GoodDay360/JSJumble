import os
import JSJumble

JSJumble.static_dir = r"C:\Users\Administrator\Documents\Microsoft Code\Python\JSJumble\static"
JSJumble.converted_dir = r"C:\Users\Administrator\Documents\Microsoft Code\Python\JSJumble\converted"
JSJumble.cache_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),"cache.sql")

JSJumble.host = "127.0.0.1"
JSJumble.port = 80
JSJumble.js_only = False
JSJumble.delete_unlisted = True

JSJumble.engine = {
    "compact": True,
    "controlFlowFlattening": False,
    "deadCodeInjection": False,
    "debugProtection": False,
    "debugProtectionInterval": 0,
    "disableConsoleOutput": True,
    "identifierNamesGenerator": "hexadecimal",
    "log": False,
    "numbersToExpressions": False,
    "renameGlobals": False,
    "selfDefending": True,
    "simplify": True,
    "splitStrings": False,
    "stringArray": True,
    "stringArrayCallsTransform": False,
    "stringArrayEncoding": [],
    "stringArrayIndexShift": True,
    "stringArrayRotate": True,
    "stringArrayShuffle": True,
    "stringArrayWrappersCount": 1,
    "stringArrayWrappersChainedCalls": True,
    "stringArrayWrappersParametersMaxCount": 2,
    "stringArrayWrappersType": "variable",
    "stringArrayThreshold": 0.75,
    "unicodeEscapeSequence": False
}

JSJumble.start()