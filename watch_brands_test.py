import argparse

brands = [
	['a. lange & sohne', 'german'],
	['accutron', 'japanese'],
	['audemars piguet', 'swiss'],
	['blancpain', 'swiss'],
	['breguet', 'swiss'],
	['breitling', 'swiss'],
	['bulova', 'japanese'],
	['carl f. bucherer', 'swiss'],
	['casio', 'japanese'],
	['chopard', 'swiss'],
	['citizen', 'japanese'],
	['eterna', 'swiss'],
	['f.p. journe', 'swiss'],
	['fortis', 'swiss'],
	['frederique constant', 'swiss'],
	['girard-perregaux', 'swiss'],
	['glycine', 'swiss'],
	['grand seiko', 'japanese'],
	['hamilton', 'swiss'],
	['hublot', 'swiss'],
	['jaeger-lecoultre', 'swiss'],
	['junghans', 'german'],
	['king seiko', 'japanese'],
	['longines', 'swiss'],
	['mb&f', 'swiss'],
	['meistersinger', 'german'],
	['mido', 'swiss'],
	['mondaine', 'swiss'],
	['movado', 'swiss'],
	['nomos', 'german'],
	['omega', 'swiss'],
	['orient', 'japanese'],
	['oris', 'swiss'],
	['patek philippe & co.', 'swiss'],
	['piaget', 'swiss'],
	['rado', 'swiss'],
	['raymond weil', 'swiss'],
	['richard mille', 'swiss'],
	['rolex', 'swiss'],
	['seiko', 'japanese'],
	['sinn', 'german'],
	['squale', 'swiss'],
	['swatch', 'swiss'],
	['tag heuer', 'swiss'],
	['tissot', 'swiss'],
	['tudor', 'swiss'],
	['vacheron constantin', 'swiss']
]

def draw_text():
    print(" ____  ____  ____  ____  ____ ")
    print("||W ||||A ||||T ||||C ||||H ||")
    print("||__||||__||||__||||__||||__||")
    print("|/__\||/__\||/__\||/__\||/__\|")
    print(" ____  ____  ____  ____  ____  ____ ")
    print("||B ||||R ||||A ||||N ||||D ||||S ||")
    print("||__||||__||||__||||__||||__||||__||")
    print("|/__\||/__\||/__\||/__\||/__\||/__\|")
    print(" ____  ____  ____  ____ ")
    print("||T ||||E ||||S ||||T ||")
    print("||__||||__||||__||||__||")
    print("|/__\||/__\||/__\||/__\|")
    print()

def parse_args():
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-s', '--swiss', dest='swiss', action='store_true')
    parser.add_argument('-j', '--japanese', dest='japanese', action='store_true')
    parser.add_argument('-g', '--german', dest='german', action='store_true')
    args = vars(parser.parse_args())
    return args

# intro
draw_text()
print('Welcome to Watch Brands Test!')
print()

# parse arguments
args = parse_args()
if args['swiss']:
    brands_test = [brand[0] for brand in list(filter(lambda brand: brand[1] == 'swiss', brands))]
elif args['japanese']:
    brands_test = [brand[0] for brand in list(filter(lambda brand: brand[1] == 'japanese', brands))]
elif args['german']:
    brands_test = [brand[0] for brand in list(filter(lambda brand: brand[1] == 'german', brands))]
else:
    brands_test = [brand[0] for brand in brands]
    
# test
score = 0
max_score = len(brands_test)
warnings = 0
max_warnings = 5
while score < max_score and warnings < max_warnings:
    guess = input('Enter a watch brand: ').strip().lower()
    if guess in brands_test:
        score+=1
        brands_test.remove(guess)
        print('Correct!')
    else:
        warnings+=1
        print(f'Incorrect! {warnings}/5 warnings.')
if score == max_score:
    print('Congratulations! You completed the test!')
else:
    print(f'You scored {score} out of {max_score}. Try again!')
