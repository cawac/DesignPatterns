namespace AbstractFactory;

public class SkeletonSolider: ISolider
{
    public int MaxHealth { get; set; } = 100;
    public int Health { get; set; } = 100;
    public int Damage { get; set; } = 10;
    public int Armor { get; } = 2;

    public void TakeDamage(int damage)
    {
        Health -= damage - this.Armor;
    }

    public void Attack(ref ICreature target)
    {
        target.TakeDamage(this.Damage);
    }
}