def get_language_names(yaml_dump: dict) -> list:
    names = [*yaml_dump.keys()]
    return names

def create_ref_table():
    ...

# EOF

if __name__ == '__main__':
    print('This module is intended to be imported, not run directly.')