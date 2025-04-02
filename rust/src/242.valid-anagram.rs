use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }

        let mut s_letter_count_map: HashMap<char, i32> = HashMap::new();
        s.chars().into_iter().for_each(|c| {
            s_letter_count_map
                .entry(c)
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
        });

        let mut t_letter_count_map: HashMap<char, i32> = HashMap::new();
        t.chars().into_iter().for_each(|c| {
            t_letter_count_map
                .entry(c)
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
        });

        for c in s.chars().into_iter() {
            if s_letter_count_map.get(&c) != t_letter_count_map.get(&c) {
                return false;
            }
        }

        return true;
    }
}
