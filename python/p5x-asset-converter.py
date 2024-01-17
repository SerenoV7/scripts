# This script can be used on P5X CBT2 and CBT3 AssetBundle files
# These files have a dummy encryption that makes them unreadable to programs like AssetStudio
# This script simply makes it so these programs can read the AssetBundles correctly

# Simply place this script inside ../client/bin/Bundles and it'll automatically convert all the AssetBundles

import os
import threading

def process_bundle_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    second_unityfs_offset = content.find(b'UnityFS', content.find(b'UnityFS') + 1)

    if second_unityfs_offset == -1:
        print(f"{file_path} is not a P5X CBT2 AssetBundle or uses different formatting/encryption method")
        return

    modified_content = content[second_unityfs_offset:]

    with open(file_path, 'wb') as file:
        file.write(modified_content)

    print(f"Finished converting {file_path}")

def process_directory(directory, num_threads):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.bundle'):
                file_path = os.path.join(root, file)
                thread = threading.Thread(target=process_bundle_file, args=(file_path,))
                thread.start()
                
                if threading.active_count() >= num_threads:
                    thread.join()

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))

    num_cores = os.cpu_count()

    if num_cores <= 6:
        num_threads = num_cores // 2
    else:
        num_threads = num_cores - 4
        
    process_directory(script_directory, num_threads)

if __name__ == "__main__":
    main()
