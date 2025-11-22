let direction1 = prompt(`Welcome to Treasure Island!
Your mission is to find the treasure.
You're at a cross road. Where do you
want to go? Type 'left' or 'right'`);

//Results and new conditional statements
if (direction1.toLowerCase() == "left"){
    let direction2 = prompt(`You've come to a lake. There is an
island in the middle of the lake.
What would you like to do? Type 'swim
towards it' or 'leave'`);
    if (direction2.toLowerCase() == "swim towards it"){
        console.log(`We regret to inform you that hostile
people found you and you're dead 💀`);
    }
    else if (direction2.toLowerCase() == "leave"){
        console.log(`You left the area but the temperature
dropped and you froze to death 💀`);
    }
    else{
        console.log(`Please type a valid direction.
Game over.`);
    }
}
else if (direction1.toLowerCase() == "right"){
    let direction2 = prompt(`You've encountered a swarm of bees!
Which direction will you run? Type
'left' or 'right'`);
    if (direction2.toLowerCase() == "left"){
        console.log(`We regret to inform you that you were
stung to death 💀`);
    }
    else if (direction2.toLowerCase() == "right"){
        let direction3 = prompt(`After running for some time, you trip
on something on the ground. What will
you do? Type 'continue' or 'investigate'`);
        if (direction3.toLowerCase() == "continue"){
            console.log(`You overexerted yourself. We regret
to inform you that you are dead 💀`);
        }
        else if (direction3.toLowerCase() == "investigate"){
            console.log(`Congratulations! You found the
treasure!!! 💰`);
        }
        else{
            console.log(`Please type a valid direction.
Game over.`);
        }
    }
    else{
        console.log(`Please type a valid direction.
Game over.`);
    }
}
else{
    console.log(`Please type a valid direction.
Game over.`);
}
