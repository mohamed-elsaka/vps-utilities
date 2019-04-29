#!/usr/bin/python
import requests
import xml.etree.ElementTree as ET

import os
import time
import subprocess
import sys, getopt


def get_item_xml_files_url(ia_item_id):
    return 'https://archive.org/download/' + str(ia_item_id) + '/' + str(ia_item_id) + '_files.xml'

def get_original_files_urls(xml_files_url):
    # files = Get all 'file' tags when source="original"
    xml_files_file = requests.get(xml_files_url, stream=True)
    xml_files_file.raw.decode_content = True  # ensure transfer encoding is honoured
    root_el = ET.parse(xml_files_file.raw).getroot()
    
    # file_url = files[i]
    original_files_urls = [];
    for file_el in root_el.findall('file'):
        if file_el.get('source') == 'original':
            # print(file_el.get('name'))
            original_files_urls.append(file_el.get('name'));
    return original_files_urls

def generate_urls_file_for_aria2(ia_item_id, original_files_urls):
    if not os.path.exists(ia_item_id):
        os.makedirs(ia_item_id)
    aria2_urls_file_name = ia_item_id + '/' + ia_item_id + '.txt'
    original_file_url_base = 'https://archive.org/download/' + ia_item_id 
    output = ""
    for index, original_file_url in enumerate(original_files_urls):
        original_file_url_full = original_file_url_base + '/' + original_file_url
        output += original_file_url_full
        output += "\n \t out=" + original_file_url + " \n" 
        output = output.encode('ascii', 'replace')

        txt = "Got " + str(index+1) + "/" + str(len(original_files_urls)) + " urls"
        sys.stdout.write("\r%s" % txt)
        sys.stdout.flush()
        # time.sleep() # move the cursor to the next line

    with open(aria2_urls_file_name, "w") as aria2_urls_file:
        aria2_urls_file.write(output )
        

def generate_dl_bash_file(ia_item_id, max_concurrent_downloads, max_connections_per_server):
    aria2_bash_file_name = ia_item_id + '/dl.sh'
    with open(aria2_bash_file_name, "w") as aria2_bash_file:
        aria2_bash_file.write('eval "aria2c -c -x' + str(max_connections_per_server) 
                                + ' -j' + str(max_concurrent_downloads) 
                                + ' -i ' + ia_item_id + '.txt";' )
    
    make_executable(aria2_bash_file_name)
    
def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)

def main(argv):
    ia_item_id = ''
    max_concurrent_downloads = 1
    max_connections_per_server = 5

    try:
      opts, args = getopt.getopt(argv,"hi:j:x:",["ia_item_id=","max_concurrent_downloads=", "max_connections_per_server="])
    except getopt.GetoptError:
        print 'ia-downloader.py -i <ia_item_id>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ia-downloader.py -i <ia_item_id>'
            sys.exit()
        elif opt in ("-i", "--ia_item_id"):
            ia_item_id = arg
            if str(ia_item_id).lower().startswith('https://') or str(ia_item_id).lower().startswith('http://'):
                path, ia_item_id = os.path.split(ia_item_id)

        elif opt in ("-j", "--max_concurrent_downloads"):
            max_concurrent_downloads = arg
        elif opt in ("-x", "--max_connections_per_server"):
            max_connections_per_server = arg

    # Get item's xml file
    print("Getting xml files file from https://archive.org/details/" + ia_item_id)    
    xml_files_url = get_item_xml_files_url(ia_item_id)

    # 15_Goal_Setting_Workshop_Closing_Remarks/081_Section15UnabriddgedWrittenVersion.pdf
    original_files_urls = get_original_files_urls(xml_files_url)
    
    generate_urls_file_for_aria2(ia_item_id, original_files_urls)

    generate_dl_bash_file(ia_item_id, max_concurrent_downloads, max_connections_per_server)

    print("\nTo start downloading... 'cd " + ia_item_id + " && ./dl.sh'")
   


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print 'ia-downloader.py -i <ia_item_id>'
