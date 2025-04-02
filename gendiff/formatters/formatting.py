from gendiff.formatters import stylish_format, plain_format, json_format

FORMATTERS = {"stylish": stylish_format, "plain": plain_format, "json": json_format}


def formatting(tree, format_):
    """
    The function checks the input format for an error.
    Displays a message in case of an error.
    If there is no error, it implements the user's
    request in the required format.
        tree (OrderDict): OrderDict with differences
        format_ (str): format output data, default=stylish
        return (str): depends on param "format_name"
    """
    if format_ not in FORMATTERS:
        raise ValueError(
            "Unsupported format. Next formats are supported: {}".format(
                FORMATTERS.keys()
            )
        )
    return FORMATTERS[format_].format(tree)
