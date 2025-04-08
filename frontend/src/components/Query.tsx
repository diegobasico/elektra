function Query() {
  const hours: number = new Date().getHours();
  let timeOfDay: string;
  if (hours >= 5 && hours < 12) {
    timeOfDay = "morning";
  } else if (hours >= 12 && hours < 19) {
    timeOfDay = "afternoon";
  } else {
    timeOfDay = "night";
  }

  return (
    <div className="p-4">
      <span className="text-3xl">Good {timeOfDay}. Let's Query!</span>
    </div>
  );
}

export default Query;
