import multiprocessing
from multiprocessing import current_process
from pathlib import Path
import logging

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

# Function to search for keywords in files
def search_files(files, keywords):
    results = {}
    for file in files:
        with file.open() as f:
            content = f.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in results:
                        results[keyword] = []
                    results[keyword].append(file)
    return results

# Function to divide files among processes
def divide_files(files, num_processes):
    file_groups = []
    for i in range(num_processes):
        file_groups.append(files[i::num_processes])
    return file_groups

# Function to perform keyword search in parallel
def parallel_search(files, keywords, num_processes):
    logger.debug(f'Started {current_process().name}')
    file_groups = divide_files(files, num_processes)
    pool = multiprocessing.Pool(processes=num_processes)
    results = pool.map(search_files_wrapper, [(files, keywords) for files in file_groups])
    pool.close()
    pool.join()
    
    # Combine results from all processes
    final_results = {}
    for result in results:
        for keyword, files in result.items():
            if keyword not in final_results:
                final_results[keyword] = []
            final_results[keyword].extend(files)
    
    return final_results

# Wrapper function to pass multiple arguments to multiprocessing.Pool.map
def search_files_wrapper(args):
    logger.debug(f'Started {current_process().name}')
    return search_files(*args)

if __name__ == "__main__":
    # List of files to search
    files = [Path("file1.txt"), Path("file2.txt"), Path("file3.txt"), Path("file4.txt"), Path("file5.txt")]
    
    # Keywords to search for
    keywords = ["keyword1", "keyword2", "keyword3"]
    
    # Number of processes to use
    num_processes = 3
    
    # Perform parallel search
    results = parallel_search(files, keywords, num_processes)
    
    # Output search results
    for keyword, files in results.items():
        print(f"Keyword '{keyword}' found in files: {[str(file) for file in files]}")
