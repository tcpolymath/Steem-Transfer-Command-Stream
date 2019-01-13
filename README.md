# Steem-Transfer-Command-Stream
Tutorial files for creating a stream to evaluate commands made in Steem transfers

This small program returns a stream of transfers to a specific account, parsed into a format friendly for use as commands to a program. Many Steem services receive commands through account transfers, and the Transfer_Command_Strem is designed to make that easier.

It returns a stream of transfers to a single account in dictionary format, containing the sending account name, the amount, the currency name, and the memo contents parsed as a list of terms separated by spaces.

This requires the Beem library: https://github.com/holgern/beem
