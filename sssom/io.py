import os

from .parsers import get_parsing_function
from .writers import get_writer_function
from .context import get_jsonld_context
import json
import logging

cwd = os.path.abspath(os.path.dirname(__file__))

def filter_predicate_file(input: str, predicates: list, output: str = None):
    """
    converts from one format to another
    :param input:
    :param output:
    :param input_format:
    :param output_format:
    :param context_path:
    :param read_func
    :param write_func
    :return:
    """
    curie_map={}
    contxt = get_jsonld_context()
    logging.error("Not implemented")

def convert_file(input: str, output: str = None, input_format: str = None, output_format: str = None, context_path=None,
                 read_func=None, write_func=None):
    """
    converts from one format to another
    :param input:
    :param output:
    :param input_format:
    :param output_format:
    :param context_path:
    :param read_func
    :param write_func
    :return:
    """
    curie_map={}
    contxt = get_jsonld_context()

    if context_path:
        if os.path.isfile(context_path):
            with open(context_path) as json_file:
                contxt = json.load(json_file)



    for key in contxt["@context"]:
        v = contxt["@context"][key]
        if isinstance(v,str):
            curie_map[key]=v
    if read_func is None:
        read_func = get_parsing_function(input_format, input)
    doc = read_func(input,curie_map=curie_map)

    if write_func is None:
        write_func, fileformat = get_writer_function(output_format, output)
    write_func(doc, output, fileformat=fileformat, context_path=context_path)
