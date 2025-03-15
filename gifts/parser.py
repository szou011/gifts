"""Read GIFTS format for the transaction statement, currently this does not support the balance statement.
"""

import os
import csv

from typing import Generator

from record_type import Transaction, Balance, AccountTotal, FileTotal

class TRNStatement:
    """A transaction statement file that includes all the debit and credit individual transctions for
    all the nominated account, as well as the balances."""

    def __init__(self, file_name: str | os.PathLike) -> None:
        self.file_name = file_name

    @property
    def lines(self) -> Generator[list[str], None, None]:
        with open(self.file_name, mode='r') as f:
            return (line.split(sep=',') for line in f.readlines())

    def get_transaction_records(self, account_number: str | None = None) -> list[Transaction | None]:
        """Return the transaction records for all accounts by default."""
        if account_number is None:
            return [Transaction(*record) for record in self.lines if record[0] == '3']
        else:
            return [Transaction(*record) for record in self.lines if record[0] == '3' if record[2] == account_number]

    def get_balances(self, account_number:str | None = None) -> list[Balance | None]:
        """Return the opening and closing balance for all accounts by default."""
        if account_number is None:
            return [Balance(*record) for record in self.lines if record[0] == '5' or record[0] == '6']
        else:
            return [Balance(*record) for record in self.lines if (record[0] == '5' or record[0] == '6') if record[2] == account_number]

    def get_account_total(self, account_number: str | None = None) -> list[AccountTotal | None]:
        """Return the total debit and credit for all accounts by default."""
        if account_number is None:
            return [AccountTotal(*record) for record in self.lines if record[0] == '8']
        else:
            return [AccountTotal(*record) for record in self.lines if record[0] == '8' if record[2] == account_number]

    def get_file_total(self) -> list[FileTotal | None]:
        """Return the total debit and credit in the file."""
        return [FileTotal(*record) for record in self.lines if record[0 =='9']]
