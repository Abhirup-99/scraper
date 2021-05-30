import os
from typing import Any, Set


def create_project_dir(directory: str) -> None:
    if not os.path.exists(directory):
        print("Creating the directory" + directory)
        os.makedirs(directory)


def create_data_files(project_name: str, base_url: str) -> None:
    queue = os.path.join(project_name, "queue.txt")
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


def write_file(path: str, data: Any) -> None:
    with open(path, "w") as f:
        f.write(data)


def append_to_file(path: str, data: Any) -> None:
    with open(path, "a") as f:
        f.write(f"{data}\n")


def delete_file_contents(path: str) -> None:
    open(path, "w").close()


def file_to_set(file_name: str) -> Set[str]:
    results = set()
    with open(file_name, "rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))
    return results


def set_to_file(links: Set[str], file_name: str) -> None:
    with open(file_name, "w") as f:
        for l in sorted(links):
            f.write(l + "\n")
