class objects:

    def __init__(self, length: float, width: float, breadth: float, weight: float):
        assert length >= 0, 'PLEASE FILL VALID VALUE ONLY'
        assert width >= 0, 'PLEASE FILL VALID VALUE ONLY'
        assert breadth >= 0, 'PLEASE FILL VALID VALUE ONLY'
        assert weight >= 0, 'PLEASE FILL VALID VALUE ONLY'
        self.length = length
        self.width = width
        self.breadth = breadth
        self.weight = weight

    def area(self):
        return self.length * self.breadth

    def volume(self):
        return self.length * self.breadth * self.width

    def converter(self):
        d = input('DO YOU WANT TO CONVERT WEIGHT TO KILOGRAMS(K) OR POUNDS(l):: ').upper()

        try:
            if d == 'L':
                kg = self.weight / 0.45
                print(f'YOUR WEIGHT IN POUNDS IS {kg} LBS')
                return kg
            if d == 'K':
                p = self.weight * 0.45
                print(f'YOUR WEIGHT IN KILOGRAMS IS {p} KILOS')
                return p
            else:
                print('GIVE VALID ANSWER ONLY MAN')
        except TypeError:
            print(f'INPUT CORRECT VALUE MAN')


lengths = int(input('PLEASE INPUT LENGTH HERE>> '))
breaths = int(input('PLEASE INPUT BREATH HERE>> '))
widths = int(input('PLEASE INPUT WIDTH HERE>> '))
weights = int(input('PLEASE INPUT WEIGHT HERE>> '))
dimensions = objects(lengths, breaths, widths, weights)
print('THE AREA OF OBJECT IS ' + '' + str(dimensions.area()) + ' ' + 'SQUARE UNITS')
print('THE VOLUME OF OBJECT IS ' + '' + str(dimensions.volume()) + ' ' + 'CUBIC UNITS')
dimensions.converter()
