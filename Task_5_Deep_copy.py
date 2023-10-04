import copy

production_config = {
    'database': {
        'host': 'prod-db-host',
        'port': 3306,
        'username': 'prod-user',
        'password': 'prod-pass'
    }
}

test_config = copy.deepcopy(production_config)
test_config['database']['host'] = 'test-db-host'
test_config['database']['port'] = '1234'

print("Original Dictionary:")
print(production_config)
print("\nAfter changes:")
print(test_config)

