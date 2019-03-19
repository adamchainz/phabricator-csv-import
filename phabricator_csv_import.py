#!/usr/bin/env python
import csv
import os

from phabricator import Phabricator


def main():
    phabricator = Phabricator(
        host='https://test-qgzwyyogzjtz.phacility.com/api/',
        # Retrieve from Personal Settings > Conduit Api Tokens
        token=os.environ['CONDUIT_API_TOKEN'],
    )
    with open('example.csv') as fp:
        next(fp)
        reader = csv.reader(fp)
        for row in reader:
            print(f"Creating task {row[0]}")
            resp = phabricator.maniphest.createtask(
                title=row[0],
                description=row[1],
            )
            print(f"    {resp['uri']}")


if __name__ == '__main__':
    main()
