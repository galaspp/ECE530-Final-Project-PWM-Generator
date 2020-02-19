`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 02/09/2020 04:44:15 PM
// Design Name: 
// Module Name: pwmGenerator
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


module pwmGenerator(
Frequency,
Duty,
CLOCK,
RESET,
EN,
pwmOut
);

//Port definitions
input [31:0]Frequency;
input [31:0]Duty;
input CLOCK, RESET, EN;
output pwmOut;



//Variable declaration
reg [31:0] count, nextCount;
reg signalOut;

//Begin module code
always @(posedge CLOCK) begin
    if(RESET) begin
        count <= 0;
    end else begin
        count <= nextCount;
    end
end

always @(count) begin
    if(count < Duty) begin
        signalOut <= 1'b1;
    end else begin
        signalOut <= 1'b0;
    end
    if(count == (Frequency - 1'b1)) begin
        nextCount <= 0;
    end else begin
        nextCount <= count + 1'b1;
    end
end
    
    
assign pwmOut = (EN && signalOut);
endmodule
