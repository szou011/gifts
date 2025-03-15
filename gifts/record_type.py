"""Record types for GIFTS transaction statement."""

from typing import NamedTuple

class Transaction(NamedTuple):
    record_type: str
    subscriber_id: str
    account_number: str
    transaction_amount: str
    serial_number: str
    transaction_code: str
    particulars: str
    code: str
    reference: str
    other_party_name: str
    transacton_date: str
    originating_bank_branch: str
    statement_indicator: str
    batch_number: str
    other_party_account_number: str

class Balance(NamedTuple):
    record_type: str
    subscriber_id: str
    account_number: str
    opening_balance: str
    spare_1: str
    spare_2: str
    record_description: str
    spare_3: str
    spare_4: str
    account_owner_name: str
    transacton_date: str


class AccountTotal(NamedTuple):
    record_type: str
    subscriber_id: str
    account_number: str
    sum_of_amounts_for_this_suffix: str
    total_number_of_transactions: str
    transaction_code: str
    record_description: str
    spare_1: str
    spare_2: str
    spare_3: str
    transacton_date: str


class FileTotal(NamedTuple):
    record_type: str
    subscriber_id: str
    nominal_account_number: str
    sum_of_amounts_for_all_suffixes: str
    total_number_of_transactions: str
    transaction_code: str
    record_description: str
    spare_1: str
    spare_2: str
    spare_3: str
    transacton_date: str
