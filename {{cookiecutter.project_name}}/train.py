import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs')
    parser.add_argument('--learning-rate', type=float, default=0.001, help='Learning rate')
    args = parser.parse_args()

    print(f"Training with epochs={args.epochs}, learning_rate={args.learning_rate}")
    # Add training logic here

if __name__ == '__main__':
    main()
