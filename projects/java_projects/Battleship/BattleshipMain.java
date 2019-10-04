import javafx.application.Application;
import javafx.animation.FadeTransition;
import javafx.geometry.Pos;
import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.Text;
import javafx.scene.text.Font;
import javafx.stage.Stage;
import javafx.util.Duration;
import java.util.Scanner;

public class BattleshipMain extends Application{
   private GridPane windowScreen = new GridPane();
   private Battleship battle;
   
   @Override
   public void start(Stage primaryStage){  
      battle = new Battleship(10, 10);
      GridPane startUp = startingGame(windowScreen);
      windowScreen = startUp;
      windowScreen.setAlignment(Pos.CENTER);
      
      Scene scene = new Scene(windowScreen, battle.getPlayerBoard().length * 65, battle.getPlayerBoard()[0].length * 55);
      primaryStage.setTitle("Battleship");
      primaryStage.setScene(scene);
      primaryStage.show();
      
      promptingPlayer();
   }
   
   public GridPane startingGame(GridPane name){
      GridPane grid = new GridPane();
      grid.setPadding(new Insets(10, 10, 10, 10));
      
      Text playerBoard = new Text("     Player Board");
      playerBoard.setFont(Font.font("Arial", 20));
      GridPane.setConstraints(playerBoard, 1, 1); //Row 1, Column 1 of GridPane
      
      int[][] p = battle.getPlayerBoard();
      
      for(int row = 0; row < p.length; row++)
      {
         for(int col = 0; col < p[row].length; col++)
         {
            Rectangle player = new Rectangle(0, 0, 20, 20);
            player.setStroke(Color.BLACK);
            if(p[row][col] == 3)
               player.setFill(Color.BLACK);
            else if(p[row][col] == 2)
               player.setFill(Color.RED);
            else if(p[row][col] == 1)
               player.setFill(Color.WHITE);
            else
               player.setFill(Color.LIGHTGRAY);
            
            grid.add(player, row + 4, col + 1); //Rows 1 - 10, Columns 4 - 13 of GridPane
         }
      }
      
      for(int i = 0; i < 2; i++)
      {
         Text blankSpace = new Text("       ");
         grid.add(blankSpace, i + 2, 1);
      }
     
      Text computerBoard = new Text("  Computer Board");
      computerBoard.setFont(Font.font("Arial", 20));
      GridPane.setConstraints(computerBoard, 1, 12); //Row 12, Column 1 of GridPane
      
      int[][] c = battle.getComputerBoardDisplay();
      
      for(int row = 0; row < p.length; row++)
      {
         for(int col = 0; col < p[row].length; col++)
         {
            Rectangle player = new Rectangle(0, 0, 20, 20);
            player.setStroke(Color.BLACK);
            if(c[row][col] == 3)
               player.setFill(Color.BLACK);
            else if(c[row][col] == 2)
               player.setFill(Color.RED);
            else if(c[row][col] == 1)
               player.setFill(Color.WHITE);
            else
               player.setFill(Color.LIGHTGRAY);
            
            grid.add(player, row + 4, col + 12); //Rows 12 - 21, Columms 4 - 13 of GridPane
         }
      } 
        
      for(int i = 0; i < 2; i++){
         Text blankSpace = new Text("       ");
         grid.add(blankSpace, i + 14, 1);
      }
     
     
      for(int i = 1; i < 11; i++){
         Text number = new Text("" + i);
         number.setFont(Font.font("Arial", 20));
         grid.add(number, 3, 11 + i);
      }
     
      for(int i = 1; i < 11; i++){
         Text numberHorizontal = new Text("" + i);
         numberHorizontal.setFont(Font.font("Arial", 20));
         grid.add(numberHorizontal, 3 + i, 11);
      }
      
      grid.getChildren().addAll(playerBoard, computerBoard);
      
      return grid;
   }
   
   public void promptingPlayer(){
   
      TextField xInput = new TextField();
      xInput.setPromptText("Enter x coordinate");
      windowScreen.add(xInput, 16, 10); //Row 10, Column 16 of GridPane
      
      TextField yInput = new TextField();
      yInput.setPromptText("Enter y coordinate");
      windowScreen.add(yInput, 16, 11); //Row 11, Column 16 of GridPane
      
      Button sendCoordinates = new Button("      Send Coordinates      ");
      windowScreen.add(sendCoordinates, 16, 12); //Row 12, Column 16 of GridPane
      sendCoordinates.setOnAction( e -> calculatingMove(xInput.getText(), yInput.getText()));       
   }
   
   public void calculatingMove(String xInput, String yInput){
      int[][] computerActual = battle.getComputerBoardHidden();
      int[][] computerDisplay = battle.getComputerBoardDisplay();
      int[][] playerBoard = battle.getPlayerBoard();
      
      boolean playerWin = false, computerWin = false, checkingHit = false;
      
      int x, y = -1;
      
      Text errorX = new Text("       Invalid x coordinate.");
      errorX.setFont(Font.font("Arial", 12));
      windowScreen.add(errorX, 16, 14);
      errorX.setOpacity(0.0);
            
      Text errorY = new Text("       Invalid y coordinate.");
      errorY.setFont(Font.font("Arial", 12));
      windowScreen.add(errorY, 16, 15);
      errorY.setOpacity(0.0);
      
      Text usedCoord = new Text("             Pick again");
      usedCoord.setFont(Font.font("Arial", 12));
      windowScreen.add(usedCoord, 16, 16);
      usedCoord.setOpacity(0.0);
            
      x = Integer.parseInt(xInput) - 1;
      y = Integer.parseInt(yInput) - 1;
      
      if( x < 0 || x > 9 )
      {
         errorX.setOpacity(1.0);
         FadeTransition fading = creatingFader(errorX);
         fading.play();
      }   
      if( y < 0 || y > 9 )
      {
         errorY.setOpacity(1.0);
         FadeTransition fading = creatingFader(errorY);
         fading.play();
      }
      
      if((x >= 0 && x <= 9) && (y >= 0 && y <= 9))
      {
         checkingHit = computerDisplay[x][y] == 0;
      }
            
      if(checkingHit)
      {
         battle.updateComputerBoards(x, y, computerActual, computerDisplay);
         playerWin = battle.checkPlayerWin();
         battle.computerTurn();
         computerWin = battle.checkComputerWin();
         updateBoards();
      }
      else
      {
         usedCoord.setOpacity(1.0);
         FadeTransition fading = creatingFader(usedCoord);
         fading.play();
      }
            
      if(playerWin)
      {
         Text playerWon = new Text("       You won!");
         playerWon.setFont(Font.font("Arial", 18));
         windowScreen.add(playerWon, 16, 18);
      }
      
      if(computerWin)
      {
         Text computerWon = new Text("   Computer won!");
         computerWon.setFont(Font.font("Arial", 18));
         windowScreen.add(computerWon, 16, 18);   
      }             
   }
   
   public void updateBoards(){
      int[][] p = battle.getPlayerBoard();
      
      for(int row = 0; row < p.length; row++)
      {
         for(int col = 0; col < p[row].length; col++)
         {
            Rectangle player = new Rectangle(0, 0, 20, 20);
            player.setStroke(Color.BLACK);
            if(p[row][col] == 3)
               player.setFill(Color.BLACK);
            else if(p[row][col] == 2)
               player.setFill(Color.RED);
            else if(p[row][col] == 1)
               player.setFill(Color.WHITE);
            else
               player.setFill(Color.LIGHTGRAY);
            
            windowScreen.add(player, row + 4, col + 1); //Rows 1 - 10, Columns 4 - 13 of GridPane
         }
      }
      
      int[][] c = battle.getComputerBoardDisplay();
      
      for(int row = 0; row < c.length; row++)
      {
         for(int col = 0; col < c[row].length; col++)
         {
            Rectangle enemy = new Rectangle(0, 0, 20, 20);
            enemy.setStroke(Color.BLACK);
            if(c[row][col] == 3)
               enemy.setFill(Color.BLACK);
            else if(c[row][col] == 2)
               enemy.setFill(Color.RED);
            else if(c[row][col] == 1)
               enemy.setFill(Color.WHITE);
            else
               enemy.setFill(Color.LIGHTGRAY);
            
            windowScreen.add(enemy, row + 4, col + 12); //Rows 12 - 21, Columms 4 - 13 of GridPane
         }
      }
   }
   
   private FadeTransition creatingFader(Node node){
      FadeTransition fade = new FadeTransition(Duration.seconds(3), node);
      fade.setFromValue(1);
      fade.setToValue(0);
      
      return fade;
   }
   
   public static void main(String[] args){
      Application.launch(args);
   }
}