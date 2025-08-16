from collections import deque

def simulate_snake(grid, start, directions, food):
    """
    Simulate a snake game in a grid based on given directions.
    
    Args:
        grid (tuple): Grid dimensions (rows, cols)
        start (tuple): Starting position (row, col)
        directions (list): List of direction commands ['U', 'D', 'L', 'R']
        food (set): Set of food positions
    
    Returns:
        list: Final snake body coordinates or 'Game Over'
    """
    rows, cols = grid
    
    # Initialize snake with starting position
    snake_body = deque([start])
    snake_set = {start}  # For O(1) collision detection
    food_set = set(food)  # Copy to avoid modifying original
    
    # Direction mappings
    direction_map = {
        'U': (-1, 0),  # Up: decrease row
        'D': (1, 0),   # Down: increase row
        'L': (0, -1),  # Left: decrease col
        'R': (0, 1)    # Right: increase col
    }
    
    print(f"Initial state: Snake at {start}, Food at {food_set}")
    
    # Process each direction command
    for i, direction in enumerate(directions):
        print(f"\nStep {i+1}: Moving {direction}")
        
        # Get current head position
        head_row, head_col = snake_body[0]
        
        # Calculate new head position
        delta_row, delta_col = direction_map[direction]
        new_head = (head_row + delta_row, head_col + delta_col)
        new_row, new_col = new_head
        
        print(f"  New head position: {new_head}")
        
        # Check wall collision
        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
            print(f"  Game Over: Hit wall at {new_head}")
            return "Game Over"
        
        # Check self collision
        if new_head in snake_set:
            print(f"  Game Over: Hit self at {new_head}")
            return "Game Over"
        
        # Move head to new position
        snake_body.appendleft(new_head)
        snake_set.add(new_head)
        
        # Check if food was eaten
        if new_head in food_set:
            print(f"  Food eaten at {new_head}! Snake grows.")
            food_set.remove(new_head)
            # Snake grows (don't remove tail)
        else:
            print("  No food eaten. Snake moves.")
            # Remove tail (snake moves without growing)
            tail = snake_body.pop()
            snake_set.remove(tail)
        
        print(f"  Snake body: {list(snake_body)}")
        print(f"  Remaining food: {food_set}")
    
    # Return final snake body as list
    final_body = list(snake_body)
    print(f"\nFinal snake body: {final_body}")
    return final_body


def visualize_grid(grid, snake_body, food_set, step_num=None):
    """Helper function to visualize the current game state"""
    rows, cols = grid
    
    # Create empty grid
    display_grid = [['.' for _ in range(cols)] for _ in range(rows)]
    
    # Place food
    for food_pos in food_set:
        row, col = food_pos
        if 0 <= row < rows and 0 <= col < cols:
            display_grid[row][col] = 'F'
    
    # Place snake body
    for i, (row, col) in enumerate(snake_body):
        if 0 <= row < rows and 0 <= col < cols:
            if i == 0:
                display_grid[row][col] = 'H'  # Head
            else:
                display_grid[row][col] = 'B'  # Body
    
    # Print grid
    if step_num is not None:
        print(f"\nGrid state after step {step_num}:")
    else:
        print("\nGrid state:")
    
    print("  " + " ".join(str(i) for i in range(cols)))
    for i, row in enumerate(display_grid):
        print(f"{i} " + " ".join(row))
    print("Legend: H=Head, B=Body, F=Food, .=Empty")


def test_snake_simulation():
    """Test the snake simulation with the provided example"""
    
    print("="*50)
    print("SNAKE GAME SIMULATION TEST")
    print("="*50)
    
    # Test case from the problem
    grid = (5, 5)
    start = (2, 2)
    directions = ['U', 'U', 'R', 'D', 'D', 'L', 'L', 'U']
    food = {(1, 2), (2, 3)}
    
    print(f"Grid size: {grid}")
    print(f"Starting position: {start}")
    print(f"Directions: {directions}")
    print(f"Food positions: {food}")
    
    # Visualize initial state
    visualize_grid(grid, [start], food, 0)
    
    # Run simulation
    result = simulate_snake(grid, start, directions, food)
    
    print(f"\nFinal result: {result}")
    
    return result


def run_additional_tests():
    """Run additional test cases"""
    
    print("\n" + "="*50)
    print("ADDITIONAL TEST CASES")
    print("="*50)
    
    test_cases = [
        {
            'name': 'Hit wall immediately',
            'grid': (3, 3),
            'start': (0, 1),
            'directions': ['U'],
            'food': set(),
            'expected': 'Game Over'
        },
        {
            'name': 'Hit self',
            'grid': (5, 5),
            'start': (2, 2),
            'directions': ['R', 'D', 'L', 'U'],
            'food': set(),
            'expected': 'Game Over'
        },
        {
            'name': 'Eat all food and survive',
            'grid': (3, 3),
            'start': (1, 1),
            'directions': ['U', 'R'],
            'food': {(0, 1), (0, 2)},
            'expected': [(0, 2), (0, 1), (1, 1)]
        },
        {
            'name': 'Simple movement without food',
            'grid': (5, 5),
            'start': (2, 2),
            'directions': ['U', 'R'],
            'food': set(),
            'expected': [(1, 3)]
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test['name']}")
        print(f"Grid: {test['grid']}, Start: {test['start']}")
        print(f"Directions: {test['directions']}, Food: {test['food']}")
        
        result = simulate_snake(test['grid'], test['start'], 
                              test['directions'], test['food'])
        
        print(f"Result: {result}")
        print(f"Expected: {test['expected']}")
        print(f"Status: {'PASS' if result == test['expected'] else 'FAIL'}")


def step_by_step_simulation(grid, start, directions, food):
    """Run simulation with step-by-step visualization"""
    
    print("\n" + "="*60)
    print("STEP-BY-STEP SIMULATION WITH VISUALIZATION")
    print("="*60)
    
    rows, cols = grid
    snake_body = deque([start])
    snake_set = {start}
    food_set = set(food)
    
    direction_map = {
        'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)
    }
    
    # Show initial state
    visualize_grid(grid, list(snake_body), food_set, 0)
    
    for i, direction in enumerate(directions, 1):
        print(f"\n{'='*30}")
        print(f"STEP {i}: Moving {direction}")
        print(f"{'='*30}")
        
        head_row, head_col = snake_body[0]
        delta_row, delta_col = direction_map[direction]
        new_head = (head_row + delta_row, head_col + delta_col)
        new_row, new_col = new_head
        
        # Check collisions
        if (new_row < 0 or new_row >= rows or 
            new_col < 0 or new_col >= cols):
            print(f"COLLISION: Hit wall at {new_head}")
            visualize_grid(grid, list(snake_body), food_set)
            return "Game Over"
        
        if new_head in snake_set:
            print(f"COLLISION: Hit self at {new_head}")
            visualize_grid(grid, list(snake_body), food_set)
            return "Game Over"
        
        # Move snake
        snake_body.appendleft(new_head)
        snake_set.add(new_head)
        
        ate_food = new_head in food_set
        if ate_food:
            print(f"FOOD EATEN at {new_head}! Snake grows.")
            food_set.remove(new_head)
        else:
            print("No food. Snake moves.")
            tail = snake_body.pop()
            snake_set.remove(tail)
        
        # Show current state
        visualize_grid(grid, list(snake_body), food_set, i)
    
    final_body = list(snake_body)
    print(f"\nFINAL RESULT: {final_body}")
    return final_body


if __name__ == "__main__":
    # Run main test
    test_snake_simulation()
    
    # Run additional tests
    run_additional_tests()
    
    # Run step-by-step visualization
    grid = (5, 5)
    start = (2, 2)
    directions = ['U', 'U', 'R', 'D', 'D', 'L', 'L', 'U']
    food = {(1, 2), (2, 3)}
    
    step_by_step_simulation(grid, start, directions, food)