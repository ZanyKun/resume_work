import java.util.Random;

public class GameOfLife
{
	private int[][] grid;
	
	public GameOfLife(int r, int c)
	{
		this.grid = new int[r][c];
	}
	
	public void randomizeInitialGrid()
	{
		Random randgen = new Random();
		for (int i = 0; i < this.grid.length; i++)
		{
			for (int j = 0; j < this.grid[i].length; j++)
			{
				this.grid[i][j] = randgen.nextInt(2);
			}
		}
	}
	
	public void blockPatternInitialGrid()
	{
		int i = this.grid.length;
		int j = this.grid[0].length;
		this.grid[i/2][j/2] = 1;
		this.grid[i/2 + 1][j/2] = 1;
		this.grid[i/2][j/2 + 1] = 1;
		this.grid[i/2 + 1][j/2 + 1] = 1;
	}
	
	public void oscillatePatternInitialGrid()
	{
		int i = this.grid.length;
		int j = this.grid[0].length;
		this.grid[i/2][j/2] = 1;
		this.grid[i/2][j/2 + 1] = 1;
		this.grid[i/2][j/2 - 1] = 1;
	}
	
	public int[][] getGrid()
	{
		return this.grid;
	}
	
	public void nextIteration()
	{
		int[][] tempgrid = new int[this.grid.length][this.grid[0].length];
		
		for (int i = 0; i < this.grid.length; i++)
		{
			for (int j = 0; j < this.grid[i].length; j++)
			{
				countAndUpdate(i, j, tempgrid);
			}
		}
		this.grid = tempgrid;
	}
	
	private void countAndUpdate(int i, int j, int[][] tempgrid)
	{
		if (i != 0 && j != 0 && i != this.grid.length - 1 && j != this.grid[i].length - 1)
		{
			int count = this.grid[i][j - 1] + this.grid[i][j + 1] + 
					this.grid[i - 1][j] + this.grid[i + 1][j] + 
					this.grid[i - 1][j + 1] + this.grid[i + 1][j + 1] +
					this.grid[i - 1][j - 1] + this.grid[i + 1][j - 1];
					
			updateTempGrid(count, i, j, tempgrid);	
		}
	}
	
	private void updateTempGrid(int count, int i, int j, int[][] tempgrid)
	{
		if ((count < 2 || count > 3) && this.grid[i][j] == 1)
			tempgrid[i][j] = 0;
		else if (count == 3 && this.grid[i][j] == 0)
			tempgrid[i][j] = 1;
		else if ((count == 2 || count == 3) && this.grid[i][j] == 1)
			tempgrid[i][j] = 1;	
	}
}