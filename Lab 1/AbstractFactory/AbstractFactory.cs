namespace AbstractFactory;

public interface IAbstractFactory
{
    ISolider CreateSolider();
    IRanger CreateRanger();
    IMagician CreateMagician();
    ICreature[] CreateSmallArmy();
    ICreature[] CreateBigArmy();
}