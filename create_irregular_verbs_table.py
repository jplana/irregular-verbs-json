import json
from tabulate import tabulate
import random

known_verbs = [
    'do',
    'feed',
    'hang',
    'take',
    'make',
    'set',
    'come',
    'have',
    'read',
    'send',
    'be',
    'begin',
    'build',
    'burn',
    'buy',
    'catch',
    'cut',
    'dig',
    'draw',
    'drink',
    'drive',
    'fall',
    'feel',
    'find',
    'eat',
    'fly',
    'forget',
    'get',
    'give',
    'go',
    'grow',
    'keep',
    'know',
    'learn',
    'let',
    'meet',
    'put',
    'ride',
    'run',
    'see'

]

def main():
    verbs_file = open('Verbs.json', 'r')
    verbs_raw = json.loads(verbs_file.read())['verbs']

    verbs = dict()
    for con in verbs_raw:
        verbs[con['Base']] = {'infinitive': con['Base'], 'simple past': con['Past-simple'], 'past participle':  con['Past-Participle']}


    head = ['Infinitive', 'Simple Past', 'Past Participle', 'Meaning']

    data = []
    for verb in known_verbs:
        chosen = random.choice(['infinitive', 'simple past', 'past participle'])
        line = list()
        for v in ['infinitive', 'simple past', 'past participle', 'meaning']:
            if v == chosen:
                line.append(verbs[verb][chosen])
            else:
                line.append('')
        data.append(line)


    print(tabulate(data, headers=head, tablefmt="grid"))



if __name__ == "__main__":
    main()
