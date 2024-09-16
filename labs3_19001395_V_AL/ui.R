library(shiny)
library(shinydashboard)

# Problem 1
closedSolutionMenuTitle <- "P1 Solución cerrada"
closedSolutionMenuId <- "closed_solution"
closedSolutionResolveBtnId <- "resolveClosedSolution"
closedSolutionResolveBtnTitle <- "Solve"
closedSolutionOutput <- "closedSolutionOut"

  # Part 2
gdMenuTitle <- "P1 GD"
gdMenuId <- "gd"
gdResolveBtnId <- "resolveGD"
gdBtnTitle <- "Solve GD"
gdOutput <- "gdOut"

  # Part 3
sgdMenuTitle <- "P1 SGD"
sgdMenuId <- "sgd"
sgdResolveBtnId <- "resolveSGD"
sgdBtnTitle <- "Solve SGD"
sgdOutput <- "sgdOut"

  # Part 4
mbgdMenuTitle <- "P1 MBGD"
mbgdMenuId <- "mbgd"
mbgdResolveBtnId <- "resolveMBGD"
mbgdBtnTitle <- "Solve MBGD"
mbgdOutput <- "mbgdOut"

# Problem 1

#Problem 2
 # Part 1
gdblsMenuTitle <- "P2 GD BLS"
gdblsMenuId <- "gdbls"
gdblsResolveBtnId <- "resolveGDBLS"
gdblsBtnTitle <- "Solve GD BLS"
gdblsOutput <- "gdblsOut"

 # Part 2
newtonBacktrackingLineSearchTitle <- "P2-2 Método Newton Backtracking line search"
newtonBacktrackingLineSearchId <- "backtracking_newton"
newtonxKTitle <- "x_k"
newtonxKId <- "xkParam"
newtonStepId <- "stepSizeParam"
newtonStepTitle <- "Step size"
newtonSolveId <- "newtonSolveP2"
newtonSolveTitle <- "Resolver"
newtonSolveOutput <- "outputNewton"

#Problem 2

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
    dashboardSidebar(
        sidebarMenu(
            menuItem(closedSolutionMenuTitle, tabName = closedSolutionMenuId),
            menuItem(gdMenuTitle, tabName = gdMenuId),
            menuItem(sgdMenuTitle, tabName = sgdMenuId),
            menuItem(mbgdMenuTitle, tabName = mbgdMenuId),
            menuItem(gdblsMenuTitle, tabName = gdblsMenuId),
            menuItem(newtonBacktrackingLineSearchTitle, tabName = newtonBacktrackingLineSearchId)
            
        )
    ),
    dashboardBody(
        tabItems(
            tabItem(closedSolutionMenuId,
                    h1(closedSolutionMenuTitle),
                    
                    actionButton(closedSolutionResolveBtnId, closedSolutionResolveBtnTitle),
                    tableOutput(closedSolutionOutput)),
            
              tabItem(gdMenuId,
                      h1(gdMenuTitle),
                      textInput("lr", "Learning Rate"),
                      textInput("numIter", "Numero de Iteraciones"),
                      actionButton(gdResolveBtnId, gdBtnTitle),
                      tableOutput(gdOutput)),

            tabItem(sgdMenuId,
                    h1(sgdMenuTitle),
                    textInput("lr", "Learning Rate"),
                    textInput("numIter", "Numero de Iteraciones"),
                    actionButton(sgdResolveBtnId, sgdBtnTitle),
                    tableOutput(sgdOutput)),
            
            tabItem(mbgdMenuId,
                    h1(mbgdMenuTitle),
                    textInput("lr", "Learning Rate"),
                    textInput("numIter", "Numero de Iteraciones"),
                    textInput("bSize", "Batch Size"),
                    actionButton(mbgdResolveBtnId, mbgdBtnTitle),
                    tableOutput(mbgdOutput)),
            
            tabItem(gdblsMenuId,
                    h1(gdblsMenuTitle),
                    textInput("lr", "Learning Rate"),
                    textInput("numIter", "Numero de Iteraciones"),
                    textInput("xInit", "X initial"),
                    actionButton(gdblsResolveBtnId, gdblsBtnTitle),
                    tableOutput(gdblsOutput)),
            tabItem(
              newtonBacktrackingLineSearchId,
              h1(newtonBacktrackingLineSearchTitle),
              box(
                textInput(newtonxKId, newtonxKTitle),
                textInput(newtonStepId, newtonStepTitle)
              ),
              actionButton(newtonSolveId, newtonSolveTitle),
              tableOutput(newtonSolveOutput)
            )
        )
    )
)
