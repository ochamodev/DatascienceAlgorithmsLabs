library(shiny)
library(shinydashboard)

# Problem 1
closedSolutionMenuTitle <- "P1 Solución cerrada"
closedSolutionMenuId <- "closed_solution"
closedSolutionResolveBtnId <- "resolveClosedSolution"
closedSolutionResolveBtnTitle <- "Solve"
closedSolutionOutput <- "closedSolutionOut"
# Problem 1

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
    dashboardSidebar(
        sidebarMenu(
            menuItem(closedSolutionMenuTitle, tabName = closedSolutionMenuId),
            menuItem("Derivación", tabName = "Derivacion")
        )
    ),
    dashboardBody(
        tabItems(
            tabItem(closedSolutionMenuId,
                    h1(closedSolutionMenuTitle),
                    
                    actionButton(closedSolutionResolveBtnId, closedSolutionResolveBtnTitle),
                    tableOutput(closedSolutionOutput)),
            
            tabItem("Derivacion",
                    h1("Diferencias Finitas"),
                    box(textInput("difFinEcu", "Ingrese la Ecuación"),
                    textInput("valorX", "x"),
                    textInput("valorH", "h")),
                    actionButton("diferFinEval", "Evaluar Derivada"),
                    textOutput("difFinitOut"))
        )
    )
)
