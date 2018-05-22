pub fn calculate(input: &str) -> (u32, u32) {
    let mut max_score = 0;
    let mut best_seq = (0, 0);
    for start in 0..input.len() {
        for end in start..input.len() {
            let slice = &input[start..end+1];
            let score: i32 = slice.chars().map(|c| {
                match c {
                    'B' => -1,
                    'R' => 1,
                    _ => panic!("Unrecognized character"),
                }
            })
            .fold(0, |res, curr| res + curr);
            println!("start: {} end: {} slice: {}", start, end, slice);
            if score.abs() > max_score {
                best_seq = (start as u32, end as u32);
                max_score = score.abs();
            }
        }
    }

    let (a, b) = best_seq;
    (a + 1, b + 1)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test1() {
        let i = "RRR";
        let actual = calculate(i);
        let expected = (1, 3);
        assert_eq!(actual, expected);
    }

    #[test]
    fn test2() {
        let i = "RRRB";
        let actual = calculate(i);
        let expected = (1, 3);
        assert_eq!(actual, expected);
    }

    #[test]
    fn test3() {
        let i = "BBRRBRRBRB";
        let actual = calculate(i);
        let expected = (3, 7);
        assert_eq!(actual, expected);
    }
}
