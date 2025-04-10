namespace AbstractFactory;

public class SkeletonRanger: IRanger
{
    public int MaxHealth { get; set; } = 50;
    public int Health { get; set; } = 50;
    public int Damage { get; set; } = 20;
    public int Armor { get; } = 1;
    public void TakeDamage(int damage)
    {
        Health -= damage - this.Armor;
    }

    public void Attack(ref ICreature target)
    {
        target.TakeDamage(this.Damage);
    }

    public void RangeAttack(ref ICreature target)
    {
        target.TakeDamage(this.Damage * 2);
    }
}