﻿namespace Builder;

internal interface ICar
{
    public string Name { get; set; }
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
}