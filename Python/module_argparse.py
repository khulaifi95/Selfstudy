import math
import argparse

parser = argparse.ArgumentParser(description='Calculate the volume of a cylinder.')
parser.add_argument('radius', type=int, help='Radius of Cylinder')
parser.add_argument('height', type=int, help='Height of Cylinder')
args = parser.parse_args()

def volume(radius, height):
    return math.pi * radius ** 2 * height

if __name__ == '__main__':
    print(volume(args.radius, args.height))

