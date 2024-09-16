
library(shiny)
library(reticulate)
use_condaenv(condaenv = "base")

source_python("algoritmos.py")

#tableOut, soluc = newtonSolverX(-5, "2x^5 - 3", 0.0001)

shinyServer(function(input, output) {
  
    #Evento y evaluación de metodo de gd
      gdCalculate<-eventReactive(input$resolveGD, {
      lr <-as.numeric(input$lr)
      numIter<-as.integer(input$numIter)
      outs<-gradient_descent()
      outs
    })
      
    #Evento y evaluación de metodo de sgd
    sgdCalculate<-eventReactive(input$resolveSGD, {
      lr <-as.numeric(input$lr)
      numIter<-as.integer(input$numIter)
      outs<-stochastic_gradient_descent(lr, numIter)
      outs
    })
    
    #Evento y evaluación de metodo de mbgd
    mbgdCalculate<-eventReactive(input$resolveMBGD, {
      lr <-as.numeric(input$lr)
      numIter<-as.integer(input$numIter)
      bSize<-as.integer(input$bSize)
      outs<-mini_batch_gradient_descent(lr,bSize, numIter)
      outs
    })
    #Evento y evaluación de metodo de gdbls
    gdblsCalculate<-eventReactive(input$resolveGDBLS, {
      xInit<-input$xInit
      outs<-gradient_descent_backtracking(xInit)
      outs
    })
    
    #Evento y evaluación de metodo de newton para ceros
    closedSolutionCalculate<-eventReactive(input$resolveClosedSolution, {
        outs<-calculate_closed_solution()
        outs
    })

    
    # Evento y evaluación de diferencias finitas
    netwonP22Calculate <- eventReactive(input$newtonSolveP2, {
      x0 <- input$xkParam[1]
      print(x0)
      stepSize <- input$stepSizeParam[1]
      print(stepSize)
      outs <- newton_method_backtrack(x0, stepSize)
      outs
    })
    
    #Render GD
    output$gdOut<-renderTable({
      gdCalculate()
    })
    
    #Render SGD
    output$sgdOut<-renderTable({
      sgdCalculate()
    })
    
    #Render MBGD
    output$mbgdOut<-renderTable({
      mbgdCalculate()
    })
    
    #Render GDBLS
    output$gdblsOut<-renderTable({
      gdblsCalculate()
    })
    
    
    #REnder metodo de Newton
    output$closedSolutionOut<-renderTable({
        closedSolutionCalculate()
    })
    
    # Render Diferncias Finitas
    output$outputNewton <- renderTable({
      netwonP22Calculate()
    })
})
