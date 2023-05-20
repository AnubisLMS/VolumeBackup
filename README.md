# Anubis Volume Backup Tool

Longhorn backup seems to be pretty damn unreliable. This is for double backups of student volumes.

## Init

```bash
./get-volumes.sh  # Generates volumes.json
python abv.py gen # Generates backup+restore job yaml with current datetime id
```

## Backup

```bash
python abv.py backup --jobs 30 --wait 60 --yes
```

## Restore

```bash
python abv.py restore --jobs 30 --wait 60 --yes
```

## Restore for specific identifier

```bash
python abv.py gen --id 20230520-025116             # Generates backup+restore job yaml with 20230520-025116
python abv.py restore --jobs 30 --wait 60 --yes    # Runs restore for everyone for id
```

## Restore for specific identifier and student

```bash
python abv.py gen --id 20230520-025116                                    # Generates backup+restore job yaml with 20230520-025116
python abv.py restore --jobs 30 --wait 60 --yes --filter abc123,xyz456    # Runs restore for abc123+xyz456 netid
```

