import sys, getopt, datetime, codecs
import re

if sys.version_info[0] < 3:
    import got
else:
    import got3 as got

def main(argv):

	if len(argv) == 0:
		print('You must pass some parameters. Use \"-h\" to help.')
		return

	if len(argv) == 1 and argv[0] == '-h':
		f = open('exporter_help_text.txt', 'r')
		print (f.read())
		f.close()

		return


	opts, args = getopt.getopt(argv, "", ("username=", "near=", "within=", "since=", "until=", "querysearch=", "toptweets", "maxtweets=", "output="))
	tweetCriteria = got.manager.TweetCriteria()
	outputFileName = "output_got.csv"

	for opt,arg in opts:
		if opt == '--username':
			tweetCriteria.username = arg
		elif opt == '--since':
			tweetCriteria.since = arg
		elif opt == '--until':
			tweetCriteria.until = arg
		elif opt == '--querysearch':
			tweetCriteria.querySearch = arg
		elif opt == '--toptweets':
			tweetCriteria.topTweets = True
		elif opt == '--maxtweets':
			tweetCriteria.maxTweets = int(arg)	
		elif opt == '--near':
			tweetCriteria.near = '"' + arg + '"'
		elif opt == '--within':
			tweetCriteria.within = '"' + arg + '"'
		elif opt == '--within':
			tweetCriteria.within = '"' + arg + '"'
		elif opt == '--output':
			outputFileName = arg
				
	outputFile = codecs.open(outputFileName, "w+", "utf-8")

	outputFile.write('username;date;retweets;favorites;text;hashtags;')

	print('Searching...\n')

	def receiveBuffer(tweets):
		for t in tweets:
			outputFile.write(('\n%s;%s;%d;%d;"%s";%s' % (t.username, t.date.strftime("%Y-%m-%d %H:%M"), t.retweets, t.favorites, t.text, t.hashtags)))
			outputFile.flush();
			print('More %d saved on file...\n' % len(tweets))

	got.manager.TweetManager.getTweets(tweetCriteria, receiveBuffer)

      
if __name__ == '__main__':
	main(sys.argv[1:])