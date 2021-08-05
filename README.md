# hybridEbooks
Markov bot for the federated universe that takes one or more corpuses as input.

To generate a corpus, use Zero's fork of Mastodon Archive (https://github.com/animeavi/mastodon-backup) and then run the resulting json through his converter (https://github.com/animeavi/fedi_ebooks/blob/master/util/fedi_archive_to_txt.rb) to remove every thing but the content of the posts.

To generate a bearer token to access the account,, use this web site (https://tinysubversions.com/notes/mastodon-bot/). Your token is the first string of random characters in the response you get from the curl command.

--NOIDED
