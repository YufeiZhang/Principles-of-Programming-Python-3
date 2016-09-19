from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--image_file', dest = 'image_filename', required = True)
parser.add_argument('--alphabet', dest = 'alphabet', required = False)
parser.add_argument('--nb_of_pixels', dest = 'nb_of_pixels', required = False)
args = parser.parse_args()

image_filename = args.image_filename
