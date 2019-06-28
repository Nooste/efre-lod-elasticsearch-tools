#!/usr/bin/python3

import sys
import json

from es2json import ArrayOrSingleValue, eprint,litter
from pymarc import MARCReader
from six.moves import zip_longest as izip_longest

def transpose_to_ldj(record):
    json_record={}
    json_record['_LEADER'] = record.leader
    json_record['_FORMAT'] = "MarcXchange"
    json_record['_TYPE'] = "Bibliographic"
    for field in record:
        if field.is_control_field():
            json_record[field.tag]=[field.data]
        else:
            ind="".join(field.indicators).replace(" ","_")
            fd={}
            for k,v in izip_longest(*[iter(field.subfields)] * 2):
                if k==".":
                    k="_"
                if v:
                    fd[k]=litter(fd.get(k),v)
            ind_obj=[]
            for k,v in sorted(fd.items()):
                ind_obj.append({k:v})
            if not field.tag in json_record:
                json_record[field.tag]=[]
            json_record[field.tag].append({ind:ind_obj})
    return json_record

def main():
    for record in MARCReader(sys.stdin.buffer.read(), to_unicode=True):
        sys.stdout.write(json.dumps(transpose_to_ldj(record))+"\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
