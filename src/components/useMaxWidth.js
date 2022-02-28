import { useState, useEffect } from "react";

export default function useMaxWidth(width) {
  const [maxWidth, setMaxWidth] = useState(false);
  useEffect(() => {
    if (window.screen.width <= width) {
      setMaxWidth(true);
    } else {
      setMaxWidth(false);
    }
    const handleResize = () => {
      if (window.innerWidth <= width) {
        setMaxWidth(true);
      } else {
        setMaxWidth(false);
      }
    };
    window.addEventListener("resize", handleResize);
    return () => {
      window.removeEventListener("resize", handleResize);
    };
  }, [width]);

  return maxWidth;
}
