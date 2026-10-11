import argparse

def main():
    parser=argparse.ArgumentParser(description='ShieldML artifact security lab')
    parser.add_argument('--version',action='version',version='ShieldML 0.1.0')
    parser.parse_args()

if __name__=='__main__':
    main()
