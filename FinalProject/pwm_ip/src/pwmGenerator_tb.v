`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/13/2020 02:22:41 PM
// Design Name: 
// Module Name: pwmGenerator_tb
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module pwmGenerator_tb;
reg [31:0]Frequency, Duty;
reg CLOCK, RESET, EN;

wire pwmOut;



    pwmGenerator pwmg(Frequency, Duty, CLOCK, RESET, EN, pwmOut);

    initial begin #0 CLOCK=0; end
    
    initial fork
        #0 RESET = 1; 
        #8 Frequency = 32'h000f;
        #8 Duty = 32'h0002;
        #12 RESET = 0;
        #50 EN = 1;
        #1000 $stop;
    join
    
always #5 CLOCK=~CLOCK; //Clock generation

endmodule
