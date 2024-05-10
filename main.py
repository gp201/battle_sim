from src.matrix import Matrix
from src.army import Army
from src.simulation import Simulation
from src.soldiers import Soldiers

def main():
    """Main function."""
    # Create a matrix
    matrix = Matrix(10, 10)
    # Create two armies
    army1 = Army("Army 1", 10, matrix)
    army2 = Army("Army 2", 10, matrix)
    # Create a simulation
    simulation = Simulation(matrix, army1, army2)
    # Run the simulation
    simulation.run()

if __name__ == "__main__":
    main()
