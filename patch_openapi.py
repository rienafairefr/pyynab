#!/usr/bin/env python3
import yaml


def main():
    with open('openapi.yaml', 'r') as openapi:
        spec = yaml.load(openapi)

    for k, v in spec['components']['schemas'].items():
        for np, p in v.get('properties', {}).items():
            pass

    spec['components']['schemas']['Account']['properties']['note']['nullable'] = True
    spec['components']['schemas']['Category']['properties']['note']['nullable'] = True
    spec['components']['schemas']['MonthSummary']['properties']['note']['nullable'] = True
    spec['components']['schemas']['Category']['properties']['goal_creation_month']['nullable'] = True
    spec['components']['schemas']['Category']['properties']['goal_target_month']['nullable'] = True
    spec['components']['schemas']['Payee']['properties']['transfer_account_id']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['category_id']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['flag_color']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['flag_color'].pop('enum', None)
    spec['components']['schemas']['TransactionSummary']['properties']['import_id']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['memo']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['payee_id']['nullable'] = True
    spec['components']['schemas']['SubTransaction']['properties']['payee_id']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['matched_transaction_id']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['transfer_account_id']['nullable'] = True
    spec['components']['schemas']['TransactionSummary']['properties']['transfer_transaction_id']['nullable'] = True
    spec['components']['schemas']['TransactionDetail']['allOf'][1]['properties']['category_name']['nullable'] = True
    spec['components']['schemas']['MonthDetail']['allOf'][1]['properties']['categories']['nullable'] = True
    spec['components']['schemas']['HybridTransaction']['allOf'][1]['properties']['payee_name']['maxLength'] = 50
    spec['components']['schemas']['ScheduledTransactionDetail']['allOf'][1]['properties']['payee_name']['maxLength'] = 50
    spec['components']['schemas']['TransactionDetail']['allOf'][1]['properties']['payee_name']['maxLength'] = 50
    spec['components']['schemas']['SaveTransaction']['properties']['payee_name']['maxLength'] = 50

    spec['components']['schemas']['TransactionSummary']['properties']['memo']['maxLength'] = 100
    spec['components']['schemas']['SaveTransaction']['properties']['memo']['maxLength'] = 100
    spec['components']['schemas']['ScheduledSubTransaction']['properties']['memo']['maxLength'] = 100
    spec['components']['schemas']['ScheduledTransactionSummary']['properties']['memo']['maxLength'] = 100
    spec['components']['schemas']['SubTransaction']['properties']['memo']['maxLength'] = 100
    try:
        spec['components']['schemas']['Category']['required'].remove('goal_type')
    except:
        pass
    spec['components']['schemas']['Category']['properties']['goal_type'].pop('enum', None)

    with open('openapi.yaml', 'w') as openapi:
        yaml.safe_dump(spec, openapi, indent=2)


if __name__ == '__main__':
    main()